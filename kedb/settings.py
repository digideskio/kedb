
import os
from os.path import abspath, dirname, join, normpath

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/kedb/db.sqlite3',
    }
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin', 'mail@newt.cz'),
)

MANAGERS = ADMINS

SITE_ID = 1
SITE_NAME = 'kedb'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'EN'),
)

USE_I18N = True

MEDIA_ROOT = '/srv/kedb/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/srv/kedb/static/'
STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'kedb.urls'

INSTALLED_APPS = (
    'django',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'rest_framework',
    'kedb',
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/etc/kedb/templates',
            '/usr/share/kedb/templates',
        ],
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/admin/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

LOGGING = {
    'version': 1,
    # When set to True this will disable all logging except
    # for loggers specified in this configuration dictionary. Note that
    # if nothing is specified here and disable_existing_loggers is True,
    # django.db.backends will still log unless it is disabled explicitly.
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(process)d %(levelname)s %(name)s '
                      '%(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/srv/kedb/logs/app.log',
            'formatter': 'verbose',
        },
    },
}

try:
    with open("/etc/kedb/settings.py") as f:
        code = compile(f.read(), "/etc/kedb/settings.py", 'exec')
        exec(code)
except IOError:
    pass

if hasattr(globals(), "LOCAL_INSTALLED_APPS"):
    INSTALLED_APPS += LOCAL_INSTALLED_APPS
