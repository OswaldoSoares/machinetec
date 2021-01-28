from machinetec.settings.settings import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET-KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': os.environ['userr'],
        'PASSWORD': os.environ['password'],
        'SERVER': os.environ['server'],
        'PORT': os.environ['port'],
        'NAME': os.environ['name'],
        'options': {
            'init_command': 'SET foreing_key_checks = 0',
        }
    }
}
