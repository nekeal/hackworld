from .base import *

DEBUG = False

DATABASES = {
    'local': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
        # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'db_name',
    #     'USER': 'db_user',
    #     'PASSWORD': 'db_password',
    #     'HOST': 'db_host',
    # }

}
MEDIA_ROOT = '/var/www/hackworld/media/'