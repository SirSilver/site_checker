"""Default configuration for celery"""

import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'checker.settings')

app = Celery('checker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
