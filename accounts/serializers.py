import uuid

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from content.models import Exam
from .models import StudentProfile, is_guest

User = get_user_model()


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Login with email + password instead of username + password."""
    username_field = 'email'

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class SignupSerializer(serializers.Serializer):
    """Create a User only — email, username, password. Kept to just these
    three fields on purpose so signup stays quick; exam/name/etc. are
    collected later as a profile-completion step (see StudentProfile),
    the same way a claimed guest account (ClaimAccountSerializer below)
    or a Google sign-in already ends up with no profile until then.
    """
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=8, write_only=True)

    def validate_email(self, value):
        value = value.lower()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("An account with this email already exists.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("That username is taken.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )


def create_guest_user():
    """Silently provision a throwaway User so a visitor can start a free
    paper with zero forms. No email, no password — just a real row so the
    normal IsAuthenticated + JWT machinery works unchanged everywhere else.
    """
    return User.objects.create_user(
        username=f'guest_{uuid.uuid4().hex}',
        password=None,  # create_user() calls set_unusable_password() for None
    )


class ClaimAccountSerializer(serializers.Serializer):
    """POST /api/auth/claim/ — turns the current guest User into a real
    account in place (same id), so their free-paper attempt history carries
    over automatically. Mirrors SignupSerializer but updates instead of
    creating.
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)
    full_name = serializers.CharField(max_length=120)
    primary_exam_id = serializers.IntegerField()
    current_class = serializers.ChoiceField(
        choices=StudentProfile.CLASS_CHOICES, required=False, allow_blank=True,
    )
    target_year = serializers.IntegerField(required=False, allow_null=True)
    city = serializers.CharField(max_length=60, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)

    def validate(self, attrs):
        user = self.context['request'].user
        if not is_guest(user):
            raise serializers.ValidationError(
                'This account is already signed up.'
            )
        return attrs

    def validate_email(self, value):
        value = value.lower()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("An account with this email already exists.")
        return value

    def validate_primary_exam_id(self, value):
        if not Exam.objects.filter(id=value, is_active=True).exists():
            raise serializers.ValidationError("Invalid exam.")
        return value

    @transaction.atomic
    def save(self):
        user = self.context['request'].user
        data = self.validated_data

        user.email = data['email']
        user.username = data['email']
        user.set_password(data['password'])
        user.save(update_fields=['email', 'username', 'password'])

        StudentProfile.objects.update_or_create(
            user=user,
            defaults=dict(
                primary_exam_id=data['primary_exam_id'],
                full_name=data['full_name'],
                current_class=data.get('current_class', ''),
                target_year=data.get('target_year'),
                city=data.get('city', ''),
                phone=data.get('phone', ''),
            ),
        )
        return user


class CompleteProfileSerializer(serializers.Serializer):
    """PATCH /api/auth/me/ the first time — when request.user has no
    StudentProfile yet. Collects what SignupSerializer deliberately left
    out (exam, name, ...), one time, once the app actually needs it
    instead of upfront at signup.
    """
    full_name = serializers.CharField(max_length=120)
    primary_exam_id = serializers.IntegerField()
    current_class = serializers.ChoiceField(
        choices=StudentProfile.CLASS_CHOICES, required=False, allow_blank=True,
    )
    target_year = serializers.IntegerField(required=False, allow_null=True)
    target_date = serializers.DateField(required=False, allow_null=True)
    city = serializers.CharField(max_length=60, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)

    def validate_primary_exam_id(self, value):
        if not Exam.objects.filter(id=value, is_active=True).exists():
            raise serializers.ValidationError("Invalid exam.")
        return value

    def save(self):
        data = self.validated_data
        return StudentProfile.objects.create(
            user=self.context['request'].user,
            primary_exam_id=data['primary_exam_id'],
            full_name=data['full_name'],
            current_class=data.get('current_class', ''),
            target_year=data.get('target_year'),
            target_date=data.get('target_date'),
            city=data.get('city', ''),
            phone=data.get('phone', ''),
        )


class PasswordResetRequestSerializer(serializers.Serializer):
    """POST /api/auth/password-reset/ — email only. Never reveals whether the
    account exists (the view always returns the same generic response)."""
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    """POST /api/auth/password-reset/confirm/ — the uid+token from the emailed
    link, plus the new password."""
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8, write_only=True)

    def validate(self, attrs):
        from django.utils.http import urlsafe_base64_decode
        from django.utils.encoding import force_str
        from django.contrib.auth.tokens import default_token_generator

        try:
            uid = force_str(urlsafe_base64_decode(attrs['uid']))
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError({'uid': 'Invalid or expired reset link.'})

        if not default_token_generator.check_token(user, attrs['token']):
            raise serializers.ValidationError({'token': 'Invalid or expired reset link.'})

        attrs['user'] = user
        return attrs

    def save(self):
        user = self.validated_data['user']
        user.set_password(self.validated_data['new_password'])
        user.save(update_fields=['password'])
        return user


class ExamMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name', 'slug']


class StudentProfileSerializer(serializers.ModelSerializer):
    primary_exam = ExamMiniSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = [
            'full_name', 'primary_exam', 'current_class',
            'target_year', 'target_date', 'city', 'phone',
            'is_email_verified', 'preferred_break_interval_minutes',
        ]


class StudentProfileUpdateSerializer(serializers.ModelSerializer):
    """PATCH /api/auth/me/ — the narrow set of fields a student can self-serve.

    Everything else on the profile stays support-managed (see Settings page
    copy) until a fuller profile-edit flow exists.
    """

    class Meta:
        model = StudentProfile
        fields = ['target_date']


class UserMeSerializer(serializers.ModelSerializer):
    """GET /api/auth/me/ — everything the frontend needs about the logged-in user.

    profile is null for guest accounts (see accounts.models.is_guest) —
    they're created with no StudentProfile until they claim the account via
    POST /api/auth/claim/. is_guest lets the frontend tell "logged in for
    real" apart from "silently provisioned to start a free paper".
    """
    profile = serializers.SerializerMethodField()
    is_guest = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'profile', 'is_guest']

    def get_profile(self, user):
        profile = getattr(user, 'profile', None)
        return StudentProfileSerializer(profile).data if profile else None

    def get_is_guest(self, user):
        return is_guest(user)