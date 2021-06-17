import requests
from bs4 import BeautifulSoup
import settings
import csv

CSV = 'velosport.csv'


def get_html(url, params=''):
    r = requests.get(url, headers=settings.HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='content-container')
    events = []

    for item in items:
        events.append(
            {
                'factory': item.find('p', class_='product-brand').get_text(strip=True),
                'name': item.find('h3', class_='product-label').get_text(strip=True),
                'picture': item.find('img', class_='product-picture').get('data-src')
            }
        )
    return events


def save_doc(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Производитель', 'Наименование', 'Ссылка'])
        for item in items:
            writer.writerow([item['factory'], item['name'], item['picture']])


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
