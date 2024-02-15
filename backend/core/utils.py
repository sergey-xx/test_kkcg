import requests
from datetime import datetime

from rates.models import Rate

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def sync_rates():
    response = requests.get(URL)
    items = response.json().get('Valute')
    date = datetime.strptime(response.json().get(
        'Timestamp')[:-6], '%Y-%m-%dT%H:%M:%S').date()
    for item in items.items():
        try:
            Rate.objects.create(
                    charcode=item[1].get('CharCode'),
                    rate=item[1].get('Value'),
                    date=date, )
        except KeyError:
            continue
    print('БД синхронизирована!')
