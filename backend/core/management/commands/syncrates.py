from django.core.management.base import BaseCommand
import requests

from rates.models import Rate

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

class Command(BaseCommand):
    """Команда для синхронизации данных."""

    help = 'Sync rates data command.'

    def handle(self, *args, **options):
        response = requests.get(URL)
        items = response.json().get('Valute')
        for item in items.items():
            try:
                rate = Rate.objects.get_or_create(
                    cur_id=item[1]['ID'],
                    num_code=item[1]['NumCode'],
                    char_code=item[1]['CharCode'],
                    name=item[1]['Name'],
                    nominal=item[1]['Nominal'],
                    value=item[1]['Value'],
                    previous=item[1]['Previous'], )
                rate[0].save()
            except KeyError('Ошибка словаря JSON'):
                continue
