from bs4 import BeautifulSoup
import requests
import settings
import csv

CSV = 'data.csv'


def get_html(url, params=''):
    r = requests.get(url, headers=settings.HEADERS, params=params)
    return r


def get_data(page_num):
    total_doors = []
    for i in range(1, page_num + 1):
        print(f'[INFO] Обработка страницы {i}')
        html = get_html(settings.URL + f'{i}')

        soup = BeautifulSoup(html.text, 'lxml')
        items = soup.find_all('div', class_='phytpj4_plp largeCard')
        doors = []
        for item in items:
            doors.append(
                {
                    'name': item.find('a', class_='bex6mjh_plp b1f5t594_plp iypgduq_plp nf842wf_plp').get('aria-label'),
                    'price': item.find('p', class_='t3y6ha_plp xc1n09g_plp p1q9hgmc_plp').text.replace('\xa0', ''),
                    'link': settings.HOST + item.find('a',
                                                      class_='bex6mjh_plp b1f5t594_plp iypgduq_plp nf842wf_plp').get(
                        'href'),
                    'article': item.find('span', class_='t3y6ha_plp sn92g85_plp p16wqyak_plp').text
                }
            )
        total_doors.extend(doors)
    return total_doors


def save_doc(items, path):
    with open(path, 'w', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена', 'Ссылка', 'Артикул'])
        for item in items:
            writer.writerow([item['name'], item['price'], item['link'], item['article']])


if __name__ == '__main__':
    data_set = get_data(9)
    save_doc(data_set, CSV)


