from user_agent import generate_user_agent
HOST = 'https://www.garmin.ru/'
URL = 'https://www.garmin.ru/watches/catalog/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/\
    signed-exchange;v=b3;q=0.9',
    'user-agent': generate_user_agent()
}
