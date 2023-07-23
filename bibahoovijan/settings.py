import os
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

with open(os.path.join(BASE_DIR, "config.json"), 'r') as f:
    config_json_obj = json.load(f)

SECRET_KEY = config_json_obj["SECRET_KEY"]

DEBUG = True if config_json_obj["DEBUG_STATUS"] == "True" else False

ALLOWED_HOSTS = config_json_obj["ALLOWED_HOSTS"]

DJANGO_DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'debug_toolbar',
    # 'django_extensions',
    'django.contrib.humanize',
]

CUSTOM_APPS = [
    'AUTH',
    'AUTH.ModuleTaskManagement',
    'AUTH.RoleCreation',
    'AUTH.TaskAssignment',
    'AUTH.UserAuthentication',
    'AUTH.LogWithAudit',
    'AUTH.AuthDashboard',
    'WEBSITE',
    'WEBSITE.Matrimony.MatrimonyLandingpage',
    'WEBSITE.WeddingPlanner.WeddingPlannerLandingpage',
    'WEBSITE.WeddingPlanner.WeddingPlannerSellerProfile',
    'WEBSITE.WeddingPlanner.WeddingPlannerSellerGig',
    'WEBSITE.WeddingPlanner.WeddingPlannerBuyerBookmark',
    'WEBSITE.WeddingPlanner.WeddingPlannerPlan',
    'CORE',
    'CORE.Matrimony.MatrimonyProfile',
    'CORE.WeddingPlanner.WpService',
    'CORE.WeddingPlanner.WpSeller',
    'CORE.WeddingPlanner.WpGig',
    'CORE.WeddingPlanner.WpRating',
    'CORE.WeddingPlanner.WpBookmark',
    'CORE.WeddingPlanner.WpPlan'
]

INSTALLED_APPS = CUSTOM_APPS + DJANGO_DEFAULT_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'bibahoovijan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path.joinpath(BASE_DIR, 'ZTemplates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'custom_tags': 'template_tag.tags'
            }
        },
    },
]

WSGI_APPLICATION = 'bibahoovijan.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config_json_obj["DB"]["NAME"],
        'USER': config_json_obj["DB"]["USER"],
        'PASSWORD': config_json_obj["DB"]["PWD"],
        'HOST': config_json_obj["DB"]["HOST"],
        'PORT': config_json_obj["DB"]["PORT"],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/GMT-6'

USE_I18N = True

USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600
SESSION_SAVE_EVERY_REQUEST = True

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
STATIC_URL = '/static/'

MEDIA_ROOT = Path.joinpath(BASE_DIR, "media")
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

INTERNAL_IPS = config_json_obj["INTERNAL_IPS"]
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True
}
if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)


ADMIN_LOGIN_URL = 'loginpage'
VISITOR_LOGIN_URL = ''
AUTH_USER_MODEL = 'UserAuthentication.User'

EMAIL_BACKEND = config_json_obj['EMAIL_BACKEND']
EMAIL_HOST = config_json_obj['EMAIL_HOST']
EMAIL_USE_TLS = config_json_obj['EMAIL_USE_TLS']
EMAIL_PORT = config_json_obj['EMAIL_PORT']
EMAIL_HOST_USER = config_json_obj['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config_json_obj['EMAIL_HOST_PASSWORD']
EMAIL_OTP_PASSWORD_RESET_RESEND_LIMIT = config_json_obj['EMAIL_OTP_PASSWORD_RESET_RESEND_LIMIT']

MOBILE_OTP_VERIFICATION_RESEND_LIMIT = 5
MOBILE_OTP_VERIFICATION_VALIDITY_MINUTES = 5
