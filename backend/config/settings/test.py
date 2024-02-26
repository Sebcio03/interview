from os import environ

from .base import *  # noqa

SECRET_KEY = environ.get(
    "DJANGO_SECRET_KEY",
    "ZKDdSiWGOTOABitsOQe2Xy6NINNKECHgP24s1mRu4oJTmKz1sMf1jWeeSgRM5mFl",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
