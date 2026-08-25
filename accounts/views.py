from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from payments.services import grant_free_promo_if_eligible_silently

from .models import is_guest
from .serializers import (
    ClaimAccountSerializer,
    CompleteProfileSerializer,
    EmailTokenObtainPairSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetRequestSerializer,
    SignupSerializer,
    StudentProfileUpdateSerializer,
    UserMeSerializer,
    create_guest_user,
)

User = get_user_model()


class GuestSessionView(APIView):
    """POST /api/auth/guest/ — silently create a throwaway account and return
    a JWT pair for it, so a visitor can start a free paper with no signup
    form. Called by the frontend right before starting free content when it
    doesn't already hold a token (guest or real).
    """
    permission_classes = [AllowAny]

    def post(self, request):
        user = create_guest_user()

        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_201_CREATED)


class ClaimAccountView(APIView):
    """POST /api/auth/claim/ — a guest upgrading to a real account (e.g. to
    buy premium). Attaches email/password/profile to the SAME user row
    behind their current guest token, so their free-paper attempt history
    carries over instead of starting fresh.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ClaimAccountSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # First-30 free promo — see payments.services. Silent: must never
        # block account claiming if it fails.
        grant_free_promo_if_eligible_silently(user, user.profile.primary_exam)

        refresh = RefreshToken.for_user(user)
        refresh['email'] = user.email

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserMeSerializer(user).data,
        }, status=status.HTTP_200_OK)


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


class SignupView(APIView):
    """POST /api/auth/signup/ — email + username + password only. Returns a
    JWT pair. Profile (exam, name, ...) is completed later — see
    ClaimAccountView's shape for what that step should collect."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        refresh['email'] = user.email

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserMeSerializer(user).data,
        }, status=status.HTTP_201_CREATED)


class MeView(APIView):
    """GET /api/auth/me/ — who am I + my profile. Frontend calls this on every app load.

    PATCH /api/auth/me/ — two different jobs depending on current state:
    - No profile yet (fresh signup, or a Google sign-in): first PATCH must
      complete it — full_name + primary_exam_id required, see
      CompleteProfileSerializer. A guest (see accounts.models.is_guest)
      still can't do this — POST /api/auth/claim/ first.
    - Profile already exists: narrow self-serve update — target_date and
      preferred_break_interval_minutes (see StudentProfileUpdateSerializer).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserMeSerializer(request.user).data)

    def patch(self, request):
        profile = getattr(request.user, 'profile', None)

        if profile is None:
            if is_guest(request.user):
                return Response(
                    {'error': 'Guest accounts have no profile — claim your account first.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer = CompleteProfileSerializer(
                data=request.data, context={'request': request},
            )
            serializer.is_valid(raise_exception=True)
            new_profile = serializer.save()

            # First-30 free promo — see payments.services. Silent: must
            # never block profile completion if it fails.
            grant_free_promo_if_eligible_silently(request.user, new_profile.primary_exam)

            return Response(UserMeSerializer(request.user).data)

        serializer = StudentProfileUpdateSerializer(
            profile, data=request.data, partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserMeSerializer(request.user).data)


class PasswordResetRequestView(APIView):
    """POST /api/auth/password-reset/ — { email } → emails a reset link if that
    account exists. Always responds 200 with the same generic message so the
    endpoint can't be used to enumerate registered emails."""
    permission_classes = [AllowAny]

    GENERIC_RESPONSE = {
        'detail': 'If an account exists for that email, a reset link has been sent.'
    }

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return Response(self.GENERIC_RESPONSE, status=status.HTTP_200_OK)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = f"{settings.FRONTEND_URL}/reset-password?uid={uid}&token={token}"

        send_mail(
            subject='Reset your ParhaiKarlo password',
            message=(
                f"We got a request to reset your ParhaiKarlo password.\n\n"
                f"Reset it here (valid for a short time, one use only):\n{reset_link}\n\n"
                f"If you didn't request this, you can safely ignore this email."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return Response(self.GENERIC_RESPONSE, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):
    """POST /api/auth/password-reset/confirm/ — { uid, token, new_password } →
    sets the new password if the uid+token pair from the emailed link is valid."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'detail': 'Password has been reset. You can now sign in.'},
            status=status.HTTP_200_OK,
        )