"""
Example local_settings.py file

This highlights the settings you *should* change when deploying to a production machine.
"""

SECRET_KEY = 'CHANGE ME'
DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
