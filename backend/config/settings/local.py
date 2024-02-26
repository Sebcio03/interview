from .base import *  # noqa

SECRET_KEY = environ.get(
    "DJANGO_SECRET_KEY",
    "ZKDdSiWGOTOABitsOQe2Xy6NINNKECHgP24s1mRu4oJTmKz1sMf1jWeeSgRM5mFl",
)
DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}
