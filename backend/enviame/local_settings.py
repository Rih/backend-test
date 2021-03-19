import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cdz&f4cc)ym%dg5=fzf4ic%ev$99i==ubvtdj$cg%dpb9pgra1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

ENVIRONMENT = 'DEVELOPMENT'

BASE_DIRR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# run inside cmd or django shell or proper virtual environment
# setup with dependency: cryptography.fernet import Fernet
# key = Fernet.generate_key()
ENCRYPT_KEY = b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'enviame',
        'USER': 'enviame',
        'PASSWORD': '654fG4gFGt43',
        'HOST': 'db',
        'PORT': '5432',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

# admins
ADMINS = [('Admin', 'rodrigo.ediaz.f@gmail.com')]

RECAPTCHA_PUBLIC_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
RECAPTCHA_PRIVATE_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

DRF_RECAPTCHA_SECRET_KEY = '<your_reCAPTCHA_secret_key>'

DRF_RECAPTCHA_VERIFY_ENDPOINT = 'https://www.google.com/recaptcha/api/siteverify'


# CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ORIGIN_ALL = False
from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = list(default_headers) + [
]


if ENVIRONMENT in ['DEVELOPMENT']:
    # CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8080',  # dev
    )
    CSRF_TRUSTED_ORIGINS = (
        'http://localhost:8080',  # dev
    )
elif ENVIRONMENT in ['PRODUCTION']:
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8080',  # dev
    )
    CSRF_TRUSTED_ORIGINS = (
        'http://localhost:8080',  # dev
    )

elif ENVIRONMENT in ['PRODUCTION']:
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8080',  # dev
    )
    CSRF_TRUSTED_ORIGINS = (
        'http://localhost:8080',  # dev
    )
