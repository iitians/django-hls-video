"""
Django settings for django_hls_video project.

Generated by 'django-admin startproject' using Django 1.9.1.
"""

import os

from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = [
    # local
    'localhost', '127.0.0.1',
    # other containers
    'daphne',
]

# bootstrap alert classes
ALERT_BASE = 'alert alert-dismissable'
MESSAGE_TAGS = {
    messages.SUCCESS: f'{ALERT_BASE} alert-success',
    messages.INFO: f'{ALERT_BASE} alert-info',
    messages.WARNING: f'{ALERT_BASE} alert-warning',
    messages.ERROR: f'{ALERT_BASE} alert-danger',
}

if os.environ.get("PROD"):
    DEBUG = False
    WEBSOCKET_PROTOCOL = "wss://"
else:
    DEBUG = True
    WEBSOCKET_PROTOCOL = "ws://"

INSTALLED_APPS = [
    # apps
    'video',

    # third-party
    'autoslug',
    'channels',
    'chunked_upload',
    'dal',
    'dal_select2',

    #django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

FILE_UPLOAD_HANDLERS = {
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
}

SUMMERNOTE_CONFIG = {
    'attachment_filesize_limit': 15000000
}

ROOT_URLCONF = 'django_hls_video.urls'
APPEND_SLASH = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_hls_video.wsgi.application'

# channels
ASGI_APPLICATION = 'django_hls_video.routing.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if os.environ.get("DB_ENV") == "dummy" and not os.environ.get("PROD"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.dummy',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': 5432,
        }
    }
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media Files
FILE_UPLOAD_PERMISSIONS = 0o644
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_URL = '/protected'
SENDFILE_REL_PATH = 'protected'
SENDFILE_ROOT = os.path.join(MEDIA_ROOT, SENDFILE_REL_PATH)

# Celery
CELERY_BROKER_URL = "redis://redis"
CELERY_RESULT_BACKEND = "redis://redis"
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

