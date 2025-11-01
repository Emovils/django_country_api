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
ALLOWED_HOSTS = ["http://localhost:5173",  # Local React app
    "https://django-country-api.onrender.com",  # Deployed backend
    ]
