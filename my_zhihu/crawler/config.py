from __future__ import absolute_import
import os
import dotenv

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

INSTALLED_APPS = [
    'zhihu',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}
