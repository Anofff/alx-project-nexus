import os
import environ

from .base import BASE_DIR

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

# Debug mode
DEBUG = env.bool("DJANGO_DEBUG", default=True)

# Secret key
SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["*"]

# PostgreSQL for Docker local development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Static & Media (local)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
