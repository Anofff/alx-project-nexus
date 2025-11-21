from base import BASE_DIR, MIDDLEWARE
import environ
import os

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = False

# Render domain is required
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[".onrender.com"])

# Use Render PostgreSQL (DATABASE_URL)
DATABASES = {
    "default": env.db("DATABASE_URL")
}

# Security for production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Static file handling with Whitenoise
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
