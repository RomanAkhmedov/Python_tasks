import requests
from bs4 import BeautifulSoup
import settings


def get_html(url, params=''):
    r = requests.get(url, headers=settings.HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='gb-event-card')
    cards = []

