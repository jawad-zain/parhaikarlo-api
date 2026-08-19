from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from .views import (
    ClaimAccountView,
    EmailTokenObtainPairView,
    GuestSessionView,
    MeView,
    PasswordResetConfirmView,
    PasswordResetRequestView,
    SignupView,
)
from .social import GoogleLogin

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('guest/', GuestSessionView.as_view(), name='guest-session'),
    path('claim/', ClaimAccountView.as_view(), name='claim-account'),
    path('login/', EmailTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
    path('google/', GoogleLogin.as_view(), name='google-login'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]