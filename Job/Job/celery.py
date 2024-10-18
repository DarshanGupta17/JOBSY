from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Job.settings')
app = Celery('Job')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup = True
app.conf.update(
    task_create_missing_queues=True,
    worker_pool='solo',
)
