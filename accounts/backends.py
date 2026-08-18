from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class EmailBackend(ModelBackend):
    """Authenticate against `email` field instead of `username`."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        # simplejwt passes the login field as `username` regardless of what
        # we name it — so `username` here is actually the email.
        email = kwargs.get('email') or username
        if email is None or password is None:
            return None
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None