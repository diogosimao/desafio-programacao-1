from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'applogfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/logs/app/app.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['applogfile'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
