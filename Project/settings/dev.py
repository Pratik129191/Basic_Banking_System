from .common import *


DEBUG = True

SECRET_KEY = "django-insecure-bue!n4j58tr&12k^b(!rl089ju^i#x-fc(d841_cux+=bjw_g!"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


