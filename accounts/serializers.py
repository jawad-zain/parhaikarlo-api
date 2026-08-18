from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from content.models import Exam
from .models import StudentProfile

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
    """Create User + StudentProfile in one atomic step."""
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

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("An account with this email already exists.")
        return value.lower()

    def validate_primary_exam_id(self, value):
        if not Exam.objects.filter(id=value, is_active=True).exists():
            raise serializers.ValidationError("Invalid exam.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        email = validated_data['email']
        user = User.objects.create_user(
            username=email,         # username is unused but required by Django default User
            email=email,
            password=validated_data['password'],
        )
        StudentProfile.objects.create(
            user=user,
            primary_exam_id=validated_data['primary_exam_id'],
            full_name=validated_data['full_name'],
            current_class=validated_data.get('current_class', ''),
            target_year=validated_data.get('target_year'),
            city=validated_data.get('city', ''),
            phone=validated_data.get('phone', ''),
        )
        return user


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
    """GET /api/auth/me/ — everything the frontend needs about the logged-in user."""
    profile = StudentProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'profile']