# settings.py
# -------------------------------------------------------
# WHAT IS THIS FILE?
# This is the MASTER CONTROL PANEL for your entire Django project.
# It tells Django:
#   - Which apps are installed
#   - What database to use
#   - What security settings to apply
#   - Many other configurations
#
# You rarely need to edit this file once it's set up correctly.
# -------------------------------------------------------

from pathlib import Path

# BASE_DIR = the root folder of your project
# Path(__file__) = the location of this settings.py file
# .resolve().parent.parent = go up two folder levels to reach the project root
BASE_DIR = Path(__file__).resolve().parent.parent


# SECRET_KEY is used by Django for security (encrypting sessions, tokens, etc.)
# In a real production app, this should be kept private and never shared.
# For learning purposes, this is fine.
SECRET_KEY = 'django-insecure-connectly-api-learning-key-mo-it152-h3101-group13'

# DEBUG = True means you see detailed error pages when something breaks.
# In a real live website, you'd set this to False.
DEBUG = True

# ALLOWED_HOSTS = which domain names can access this app.
# '*' means any host — fine for local development.
ALLOWED_HOSTS = ['*']


# INSTALLED_APPS = all the apps Django knows about and uses.
# Think of this as a list of "plugins" that are active.
INSTALLED_APPS = [
    'django.contrib.admin',          # The admin panel at /admin/
    'django.contrib.auth',           # User authentication system
    'django.contrib.contenttypes',   # Framework for content types
    'django.contrib.sessions',       # Session management
    'django.contrib.messages',       # Flash messages
    'django.contrib.staticfiles',    # Serving CSS/JS/image files
    'rest_framework',                # Django REST Framework (DRF) ← our API toolkit
    'connectly_api',                 # OUR APP ← this is what we built
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

# ROOT_URLCONF = the main URL file for the whole project
ROOT_URLCONF = 'connectly_project.urls'

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

WSGI_APPLICATION = 'connectly_project.wsgi.application'


# DATABASE SETTINGS
# We're using SQLite — a simple file-based database.
# Perfect for learning and development.
# The database is stored as a single file: db.sqlite3
# (You'll see this file appear in your project folder after running migrations)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Timezone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'  # Philippine time ✓
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST FRAMEWORK SETTINGS
# This configures how DRF behaves globally.
REST_FRAMEWORK = {
    # DEFAULT_RENDERER_CLASSES = how responses are formatted
    # JSONRenderer = always return JSON (clean, no browser interface)
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # shows a nice web UI at each endpoint
    ],
}
