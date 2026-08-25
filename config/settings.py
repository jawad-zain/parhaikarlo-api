"""
Django settings for config project.
"""

from decouple import config
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
GROQ_API_KEY = config('GROQ_API_KEY')
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='localhost,127.0.0.1',
    cast=lambda v: [h.strip() for h in v.split(',') if h.strip()],
)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',                              # allauth requirement

    # Third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_extensions',
    'storages',
    'rest_framework.authtoken',
    'founder',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    # Our apps
    'accounts',
    'content',
    'quiz',
    'ai_tutor',
    "payments",
    "blog",
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',              # ← ADD THIS AS FIRST ITEM
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# --- Email ---
# Dev default: prints emails to the runserver console instead of sending them —
# no credentials needed. To send real email (e.g. via Gmail SMTP), set these in
# .env: EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend, EMAIL_HOST=
# smtp.gmail.com, EMAIL_PORT=587, EMAIL_USE_TLS=True, EMAIL_HOST_USER=you@gmail.com,
# EMAIL_HOST_PASSWORD=<16-char Google App Password> (not your normal password).
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='ParhaiKarlo <no-reply@parhaikarlo.local>')

# Base URL of the Next.js frontend — used to build the link inside reset emails.
FRONTEND_URL = config('FRONTEND_URL', default='http://localhost:3000')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # keep for admin browsable API testing
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': True,       # new refresh token on every /refresh call
    'BLACKLIST_AFTER_ROTATION': True,    # old refresh token becomes invalid — enables single-active-session later
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailBackend',                     # try email first (frontend/JWT flow)
    'allauth.account.auth_backends.AuthenticationBackend', # allauth (needed for Google Sign-In)
    'django.contrib.auth.backends.ModelBackend',          # fallback for admin username login
]


# --- allauth ---
ACCOUNT_EMAIL_VERIFICATION = 'none'         # trust Google's verified email; no confirmation email needed
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_UNIQUE_EMAIL = True

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'   # Google already verified it
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_AUTO_SIGNUP = True            # skip intermediate "confirm signup" page — critical for pure API flow
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }
}

# --- CORS ---
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:3000,http://127.0.0.1:3000,https://parhaikarlo-web.vercel.app',
    cast=lambda v: [o.strip() for o in v.split(',') if o.strip()],
)
CORS_ALLOW_CREDENTIALS = True

# --- dj-rest-auth: use JWT, not session cookies ---
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY': False,             # frontend needs the token in JS; not stored in HttpOnly cookie
    'JWT_AUTH_RETURN_EXPIRATION': True,
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer',
}

# --- Media storage ---
# Dev default: served straight off local disk. In production, flip
# USE_S3_MEDIA=True in .env and point the B2_* vars at a Backblaze B2
# bucket (S3-compatible) — QuestionImage.image and every other FileField/
# ImageField then read/write the bucket transparently, no code changes.
# One-time backfill of files already on local disk: manage.py sync_media_to_storage
USE_S3_MEDIA = config('USE_S3_MEDIA', default=False, cast=bool)

if USE_S3_MEDIA:
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    AWS_ACCESS_KEY_ID = config('B2_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('B2_APPLICATION_KEY')
    AWS_STORAGE_BUCKET_NAME = config('B2_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = config('B2_ENDPOINT_URL')       # e.g. https://s3.us-west-004.backblazeb2.com
    AWS_S3_REGION_NAME = config('B2_REGION', default='us-west-004')
    AWS_DEFAULT_ACL = None          # B2 bucket visibility is set at the bucket level, not per-object ACL
    AWS_QUERYSTRING_AUTH = False    # plain public URLs (not signed) — bucket must be set to public
    AWS_S3_FILE_OVERWRITE = False   # don't clobber a file if two uploads land on the same name

    # Optional: a custom/CDN domain fronting the bucket (e.g. Cloudflare in front
    # of B2 to avoid its egress cost). Leave B2_CUSTOM_DOMAIN unset to serve
    # straight from the B2 endpoint.
    _custom_domain = config('B2_CUSTOM_DOMAIN', default='')
    MEDIA_URL = (
        f'https://{_custom_domain}/'
        if _custom_domain
        else f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/'
    )
else:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"