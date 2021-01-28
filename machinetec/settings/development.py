from machinetec.settings.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a(o25lb!%pg=6y@tcy_1d$0((dp_kj8&nljt2@l&uf^6-id^c_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'S1c9c1p0',
        'SERVER': 'localhost',
        'PORT': 3306,
        'NAME': 'machinetec',
        'options': {
            'init_command': 'SET foreing_key_checks = 0',
        }
    }
}