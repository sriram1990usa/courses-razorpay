import mimetypes
from pathlib import Path
import os
#from dotenv import load_dotenv
#load_dotenv(os.path.join(BASE_DIR, ".env"))
import dj_database_url
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'change me'
if SECRET_KEY in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proj.app',
    'rest_framework',
    #'snippets'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proj.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'proj.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
DATABASE_URL = os.environ.get("DATABASE_URL")
#DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}

#DATABASES = {"default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),}
MAX_CONN_AGE = 1800

#PGPASSWORD=<password> psql -h <host> -U <user> -p <port> -d <database>
#postgresql://[user[:password]@][netloc][:port][/dbname]
#postgresql:
# //postgres     user
# :********      password
# @containers-us-west-53.railway.app     netloc
# :6859           port
# /railway        dbname
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'gboKoPTR0i6jC4TyAYtq',
        'HOST': 'containers-us-west-53.railway.app',
        'PORT': '6859',
    }
}
'''
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },  
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
USE_L10N = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
mimetypes.add_type("text/css", ".css", True)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

KEY_ID='change me'
if KEY_ID in os.environ:
    KEY_ID = os.environ["KEY_ID"]
KEY_SECRET='change me'
if KEY_SECRET in os.environ:
    KEY_SECRET = os.environ["KEY_SECRET"] 
