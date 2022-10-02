import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# app.conf.update(
#     CELERYBEAT_SCHEDULE={
#         'fetch_and_save': {
#             'task': 'path.to.your.fetching_script',
#             'schedule': crontab(minute='*/15'),
#         }
#     }
# )


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
