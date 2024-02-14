from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
from celery import shared_task
from django.conf import settings

from core.utils import sync_rates

User = get_user_model()


@shared_task()
def daily_task():
    sync_rates()


def schedule_task():
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='*',
        hour='*',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*', )
    PeriodicTask.objects.create(crontab=schedule,
                                name='send_emails',
                                task='core.tasks.daily_task')
