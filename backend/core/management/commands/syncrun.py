from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from core.tasks import schedule_task

User = get_user_model()


class Command(BaseCommand):
    """Команда для запуска синхронизации по CRON."""

    help = 'Sync data CRON.'

    def add_arguments(self, parser):
        parser.add_argument("cron", nargs="+", type=str)

    def handle(self, *args, **options):
        cron = options['cron'][0]
        schedule_task(cron)
        print(f'Синхронизация курсов активирована с расписанием "{cron}" ')
