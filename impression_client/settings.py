"""
This module is designed to do 2 things:

 1. Provide an interface (``get_setting``) for getting settings from
    ``django.conf.settings`` with settings in this file being the fallback
    default.
 2. Provide enough settings for this app to run as a standalone project.
"""

import os
import sys

from django.conf import settings


def get_setting(name):
    """
    Hook for getting Django settings and using properties of this file as the
    default.
    """
    me = sys.modules[__name__]
    return getattr(settings, name, getattr(me, name, None))


# app-specific settings
IMPRESSION_CLIENT_DEFAULT_SERVICE = "default"
IMPRESSION_CLIENT_DEFAULT_TARGET = "http://127.0.0.1:8000/api/send_message/"
IMPRESSION_CLIENT_DEFAULT_TOKEN = ""

EMAIL_BACKEND = "impression_client.backends.RemoteEmailBackend"


# standalone settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "not-a-very-good-secret"
DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [
    "impression_client",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "impression_client.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
WSGI_APPLICATION = "impression_client.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = "/static/"
APPEND_SLASH = True

# local development settings
try:
    from .local_settings import *
except ImportError:
    pass

# test settings
if "test" in sys.argv:
    try:
        from .test_settings import *
    except ImportError:
        pass
