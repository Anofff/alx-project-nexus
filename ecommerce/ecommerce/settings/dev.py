from base import BASE_DIR
import environ
import os

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = True

ALLOWED_HOSTS = ["*"]

# PostgreSQL for local development
DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default=f"postgres://{env('DB_USER', default='postgres')}:{env('DB_PASSWORD', default='postgres')}@{env('DB_HOST', default='127.0.0.1')}:{env('DB_PORT', default='5432')}/{env('DB_NAME', default='ecommerce_db')}"
    )
}

# Static & Media (local)
STATIC_URL = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
