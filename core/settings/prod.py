from .base import *

DEBUG = False
ALLOWED_HOSTS = ["kmkz.io"]

# Seguridad adicional para producción
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Puedes agregar CORS si el frontend está en otro dominio
CORS_ALLOWED_ORIGINS = [
    "https://kmkz.io",  # Ajusta según el dominio real del frontend
]

# Ajuste de nivel de logging para producción
LOGGING['handlers']['systemout_file']['level'] = 'WARNING'
LOGGING['loggers']['filemon']['level'] = 'WARNING'
LOGGING['loggers']['django.request']['level'] = 'ERROR'
