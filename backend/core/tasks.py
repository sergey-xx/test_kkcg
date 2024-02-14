from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from celery import shared_task

from core.utils import sync_rates

User = get_user_model()


@shared_task()
def daily_task():
    sync_rates()


def schedule_task(cron='1 0 * * *'):
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=cron.split()[0],
        hour=cron.split()[1],
        day_of_week=cron.split()[2],
        day_of_month=cron.split()[3],
        month_of_year=cron.split()[4], )
    PeriodicTask.objects.create(crontab=schedule,
                                name='send_emails',
                                task='core.tasks.daily_task')
