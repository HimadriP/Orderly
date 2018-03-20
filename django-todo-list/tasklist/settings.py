"""
Django settings for todolist project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('TASKLIST_SECRET_KEY')
SECRET_KEY = '2h9d82%(#5u$)-5!pj4=d2m#=#m&amp;hbp%-+bma(nlun3b5$z#w2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.humanize',
    'crispy_forms',
    'django_tables2',
    'tasks',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tasklist.urls'

WSGI_APPLICATION = 'tasklist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

SQLITE_DB = os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SQLITE_DB,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'Asia/Dubai'

USE_I18N = True

USE_L10N = False

USE_TZ = True

SHORT_DATE_FORMAT = 'N j, Y'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'assets'),
        )

STATIC_ROOT = os.path.join(BASE_DIR, "static")

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
        )

TEMPLATE_CONTEXT_PROCESSORS = (
         "django.contrib.auth.context_processors.auth",
         "django.core.context_processors.debug",
         "django.core.context_processors.i18n",
         "django.core.context_processors.media",
         "django.core.context_processors.static",
         "django.core.context_processors.tz",
         "django.core.context_processors.request",
         "tasks.context_processors.task_count"
        )

LOGIN_URL = reverse_lazy('login')

LOGIN_REDIRECT_URL = reverse_lazy('list_tasks')

SITE_ID = 1
