from bs4 import BeautifulSoup
import requests
import settings
import csv

CSV = 'data_clothes.csv'


def get_html(url, params=''):
    r = requests.get(url, headers=settings.HEADERS, params=params)
    return r


def get_data(page_num):
    total_items = []
    for i in range(1, page_num + 1):
        print(f'[INFO] Обработка страницы {i}')
        html = get_html(settings.URL + f'{i}')

        soup = BeautifulSoup(html.text, 'lxml')
        items = soup.find_all('div',
                              class_='grid-view-item')
        clothes = []
        for item in items:
            clothes.append(
                {
                    'brand': item.find('div', class_='product-grid--vendor-text').text,
                    'name': item.find('p', class_='product-grid--title').find('a').text,
                    'price': item.find('span', class_='money').text.rstrip(' руб.').replace('.', ''),
                    'link': settings.HOST + item.find('a', class_='grid__image grid__image__match').get('href'),
                    'color': item.find('p', class_='product-grid-color-item').text
                }
            )
        total_items.extend(clothes)
    return total_items


def save_doc(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Брэнд', 'Название', 'Цена', 'Ссылка', 'Цвет'])
        for item in items:
            writer.writerow([item['brand'], item['name'], item['price'], item['link'], item['color']])


if __name__ == '__main__':
    data_set = get_data(29)
    save_doc(data_set, CSV)
