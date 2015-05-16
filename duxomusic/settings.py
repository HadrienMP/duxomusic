import os

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for duxomusic project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.urandom(24).encode("hex")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', False))

TEMPLATE_DEBUG = bool(os.environ.get('DEBUG', False))

ALLOWED_HOSTS = ['duxomusic.com', 'duxomusic.fr', 'www.duxomusic.com', 'www.duxomusic.fr', 'dux2.hadrienmp.fr']

BASE_URL = os.environ['BASE_URL']


# Application definition
ROOT_URLCONF = 'duxomusic.urls'

WSGI_APPLICATION = 'duxomusic.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(DATA_DIR, 'media'))
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(DATA_DIR, 'static'))
STATIC_URL = os.environ.get('STATIC_URL', '/static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'duxomusic', 'static'),
)
SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'aldryn_boilerplates.context_processors.boilerplate',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'duxomusic', 'templates'),
)

INSTALLED_APPS = (

    # Django cms
    'djangocms_admin_style',
    'djangocms_text_ckeditor',

    # Core
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',

    # Django cms
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'treebeard',
    'reversion',

    # Filer
    'filer',
    'easy_thumbnails',

    # Colorfield
    'colorfield',

    # Aldryn Bootstrap
    'aldryn_bootstrap3',

    # Django robots
    'robots',

    # Nephila blog
    'cmsplugin_filer_image',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'django_select2',
    'meta',
    'meta_mixin',
    'admin_enhancer',
    'djangocms_blog',

    # Custom
    'duxomusic',
    'contact',
    'raw_html',
    'newsletter',
    'title_divider',
    'nm_msgs',
    'dux_news',
    'biography',
)

LANGUAGE_CODE = 'fr'
LANGUAGES = (
    ## Customize this
    ('fr', gettext('fr')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'fr',
            'hide_untranslated': False,
            'name': gettext('fr'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

CMS_SEO_FIELDS = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DATABASE_NAME', os.path.join(BASE_DIR, 'db.sqlite')),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', ''),
    }
}

MIGRATION_MODULES = {
    'menus': 'menus.migrations_django',
    'filer': 'filer.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'aldryn_bootstrap3': 'aldryn_bootstrap3.migrations_django',
}

# Session for nm_msgs

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'  # class to serialize session data
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Mail configuration

EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', True)
EMAIL_HOST = os.environ.get('EMAIL_HOST', "")
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', "")
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', "")
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
DEFAULT_FROM_EMAIL = "Dux'O <duxo@duxomusic.com>"

# EASY THUMBNAILS + Filer

FILER_DEBUG = True

FILER_ENABLE_LOGGING = True

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

FILER_DUMP_PAYLOAD = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    # 'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_HIGH_RESOLUTION = False

THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/opt/local/bin/optipng {filename}',
    'gif': '/opt/local/bin/optipng {filename}',
    'jpeg': '/opt/local/bin/jpegoptim {filename}',
}

THUMBNAIL_DEBUG = True

# Nephila Blog

PARLER_LANGUAGES = {
    1: (
        {'code': 'fr', },
    ),
}

META_SITE_PROTOCOL = os.environ.get('META_SITE_PROTOCOL', 'http')
META_SITE_DOMAIN = ALLOWED_HOSTS[0]