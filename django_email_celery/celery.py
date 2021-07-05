import os
from datetime import timedelta

from celery import Celery

# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_email_celery.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('django_email_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    "sending email": {
        "task": "send_email_task",  # <---- Name of task
        "schedule": crontab(
            minute='*'
        )
    }, "Print hello": {
        "task": "hello_task",  # <---- Name of task
        "schedule": timedelta(seconds=30)
    }, "Write a file": {
        "task": "write_task",  # <---- Name of task
        "schedule": timedelta(seconds=30)
    }
}
