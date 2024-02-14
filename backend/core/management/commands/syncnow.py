from django.core.management.base import BaseCommand

from core.tasks import daily_task

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


class Command(BaseCommand):
    """Команда для моментальной синхронизации данных."""

    help = 'Sync rates data command.'

    def handle(self, *args, **options):
        daily_task.delay()
