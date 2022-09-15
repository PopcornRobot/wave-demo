from .base import *

print("---- production.py")
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

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

