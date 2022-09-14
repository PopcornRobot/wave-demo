from .base import *

print("--- from local")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DATABASE_NAME"), 
        'USER': env("DATABASE_USER"), 
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': env("DATABASE_HOST"), 
        'PORT': '5432',
    }
}