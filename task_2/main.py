import requests
from bs4 import BeautifulSoup
import settings
import csv

CSV = 'events.csv'


def get_html(url, params=''):
    r = requests.get(url, headers=settings.HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='gb-event-info')
    events = []

    for item in items:
        events.append(
            {
                'title': item.find('h3', class_='gb-event-info__title').get_text(strip=True),
                # 'date_time': item.find('div', class_='gb-event-info__datetime'),
                'link_event': settings.HOST + item.find('h3', class_='gb-event-info__title').find('a').get('href'),
                'author': item.find('a', class_='gb-event-info__author').get_text(strip=True)
            }
        )
    return events


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название мероприятия', 'Ссылка на мероприятие', 'Автор'])
        for item in items:
            writer.writerow([item['title'], item['link_event'], item['author']])


def parser():
    pagination = int(input('Кол-во страниц для парсинга: ').strip())
    html = get_html(settings.URL)
    if html.status_code == 200:
        events = []
        for page in range(1, pagination + 1):
            print(f'Парсим страницу {page}')
            html = get_html(settings.URL, params={'page': page})
            events.extend(get_content(html.text))
            save_doc(events, CSV)
        return events
    else:
        print('Error')


print(parser())
