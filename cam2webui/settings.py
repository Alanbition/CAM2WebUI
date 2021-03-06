"""
Django settings for herokudemo project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR =  os.path.dirname(PROJECT_ROOT)
import sys



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
ADMINS = [('Yutong', 'huang_yutong@outlook.com')]

# Application definition

INSTALLED_APPS = [
    'email_system',
    'app.apps.AppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'social_django',
]

MIDDLEWARE = [
    'app.middleware.basicauth.BasicAuthMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'cam2webui.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'app/static/app'),
)
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

WSGI_APPLICATION = 'cam2webui.wsgi.application'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'client_encoding': 'UTF8',
        'default_transaction_isolation': 'read committed'
    }
}
# Update database configuration with $DATABASE_URL.
DATABASE_URL = os.environ["DATABASE_URL"]
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    GOOGLE_RECAPTCHA_SECRET_KEY = os.environ['RECAPTCHA_TEST_PRIVATE_KEY']

else:
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    GOOGLE_RECAPTCHA_SECRET_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']



# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True




# Django social authentication
# http://python-social-auth.readthedocs.io/en/latest/configuration/
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_ERROR_URL = '/register/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/oauthinfo/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_GITHUB_KEY = os.environ['GITHUB_KEY']
SOCIAL_AUTH_GITHUB_SECRET = os.environ['GITHUB_SECRET']


# Basic auth
# https://djangosnippets.org/snippets/2468/

BASICAUTH_USERNAME = os.environ['BASICAUTH_USERNAME']
BASICAUTH_PASSWORD = os.environ['BASICAUTH_PASSWORD']

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'


# Google API KEY and Auth
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']


#Email system
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #For testing. Email will not be sent, only shown in console
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_SSL = True
SERVER_EMAIL = os.environ['EMAIL_HOST_USER']
DEFAULT_FROM_EMAIL = os.environ['EMAIL_HOST_USER']
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Release settings
SECURE_BROWSER_XSS_FILTER = True


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['GOOGLE_LOGIN_KEY']
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['GOOGLE_LOGIN_SECRET']
