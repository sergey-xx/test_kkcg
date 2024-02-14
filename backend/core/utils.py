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
                    cur_id=item[1]['ID'],
                    num_code=item[1]['NumCode'],
                    charcode=item[1]['CharCode'],
                    name=item[1]['Name'],
                    nominal=item[1]['Nominal'],
                    rate=item[1]['Value'],
                    previous=item[1]['Previous'],
                    date=date, )
        except KeyError:
            continue
    print('БД синхронизирована!')
