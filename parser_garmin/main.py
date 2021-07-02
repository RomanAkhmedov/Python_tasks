from bs4 import BeautifulSoup
import requests
import settings
import csv

CSV = 'garmin_devices.csv'


def get_html(url, params=''):
    r = requests.get(url, headers=settings.HEADERS, params=params)
    with open('garmin.html', 'w') as file:
        file.write(r.text)
    return r


def get_data():
    with open('garmin.html', 'r') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        data = soup.find_all('li', class_='element')
        information = []

        for el in data:
            information.append(
                {
                    'name': el.find('div', class_='name').text,
                    'price': el.find('div', class_='price').text.split(' руб ', 1)[0].replace(' руб', '') if el.find(
                        'div', class_='price') is not None else '',
                    'low_price': el.find('div', class_='price').text.replace(' \xa0\xa0\xa0', '')[
                                 el.find('div', class_='price').text.replace(' \xa0\xa0\xa0', '').find(
                                     'б') + 1:].replace(' руб', '') if el.find('div',
                                                                               class_='price') is not None else '',
                    'link': settings.HOST + el.find('a').get('href')
                }
            )
    return information


def save_doc(data, path):
    with open(path, 'w', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена', 'Цена со скидкой', 'Ссылка'])
        for item in data:
            writer.writerow([item['name'], item['price'], item['low_price'], item['link']])


if __name__ == '__main__':
    get_html(settings.URL)
    save_doc(get_data(), CSV)
