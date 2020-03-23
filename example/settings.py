import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get("DEBUG", "") == "1"

SECRET_KEY = "qafp&j$vony2t+#z8(*3y&wmnmg6$j@uh&xg9kkr9h_x&t%wh#"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "example.core",
]

MIDDLEWARE = [
    "example.core.middleware.IntegrityMiddleware",
]

ROOT_URLCONF = "example.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}
