"""
Django settings for technites project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR= os.path.dirname(__file__)
BASE = os.path.abspath(os.path.dirname(__name__))
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)


import os.path
TEMPLATE_DIRS=(
                 os.path.join(os.path.dirname(__file__), 'templates') .replace('\\', '/') ,
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$5no+j$2dokfm)wgh&o(9_y1)6f8w1am*cc5*p+&0#y830wbu@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '127.0.0.1:8000', 'localhost:8000', '*',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'blog',
    'tinymce',
    'galeria',
    )


STATIC_URL='/static/'
STATICFILES_DIRS = (
   '/home/akanksha/Django-1.6.5/technites/static_dir/',
     # or whatever you named it
)


STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',)


ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'technites.urls'

WSGI_APPLICATION = 'technites.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



MEDIA_ROOT= os.path.join(PROJECT_PATH, 'media')

MEDIA_URL= '/media/'





STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',)


ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_CONTEXT_PROCESSORS = (
    
    'django.core.context_processors.static',
     'django.contrib.auth.context_processors.auth',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
	
	'NAME': 'technites.db',
	'USER': '',
	'PASSWORD': '',
	'HOST': '',
	'PORT': '',
}
}
