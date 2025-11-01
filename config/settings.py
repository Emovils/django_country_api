# config\settings.py


INSTALLED_APPS = [
    # Third-party apps
    'corsheaders',
    'rest_framework',

    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your app
    'citizens',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ Allow your local React app and Render backend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Local React app
    "https://django-country-api.onrender.com",  # Deployed backend
]

# ✅ CSRF trusted origins (for HTTPS)
CSRF_TRUSTED_ORIGINS = [
    "https://django-country-api.onrender.com",
]



#  Allow Render host + localhost
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "django-country-api.onrender.com",
]

ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add custom template directories here if needed
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


DEBUG = True
import os
from pathlib import Path

# -----------------------------------------
# BASE DIRECTORY
# -----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------------------------
# SECURITY SETTINGS
# -----------------------------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key-here')

DEBUG = True  # ⚠️ Set to False in production!

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "django-country-api.onrender.com",
]


# -----------------------------------------
# INSTALLED APPS
# -----------------------------------------
INSTALLED_APPS = [
    # Third-party apps
    'corsheaders',
    'rest_framework',

    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'citizens',
]


# -----------------------------------------
# MIDDLEWARE
# -----------------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must come first for CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -----------------------------------------
# URLS / WSGI
# -----------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# -----------------------------------------
# TEMPLATES
# -----------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add custom template directories here if needed
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


# -----------------------------------------
# DATABASE CONFIGURATION
# -----------------------------------------
# Use SQLite locally; override with Postgres on Render
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -----------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------------------------
# INTERNATIONALIZATION
# -----------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -----------------------------------------
# STATIC FILES (CSS, JS, Images)
# -----------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Optional: if you want local dev static directory too
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# -----------------------------------------
# CORS / CSRF SETTINGS
# -----------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Local React app
    "https://django-country-api.onrender.com",  # Deployed backend
]

CSRF_TRUSTED_ORIGINS = [
    "https://django-country-api.onrender.com",
]


# -----------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -----------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
