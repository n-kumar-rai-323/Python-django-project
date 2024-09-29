from .base import *
from django.contrib.messages import constants as messages

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p@z(*sxwb%&3i7m9=qolu!k-0wuc005p3!6jqc-jsvq)%m*pz$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#dpythonatabases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nexusdbb',
        'USER' : 'postgres',
        'PASSWORD': 1234,
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS:'alert-success',
    messages.WARNING:'alert-warning',
    messages.ERROR:'alert-danger',
}



EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '99e370e443f5e8'
EMAIL_HOST_PASSWORD = '97b9508f9f720b'
EMAIL_PORT = '2525'