from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from celery import shared_task
from django.conf import settings

User = get_user_model()


@shared_task()
def daily_task():
    pass
    
