# 1) Создать консольную программу-парсер, с выводом прогноза погоды. Дать
# возможность пользователю получить прогноз погоды в его локации ( по
# умолчанию) и в выбраной локации, на определенную пользователем дату.

import requests
from bs4 import BeautifulSoup


def get_weather(url, specific_day=False):
    result = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    city = soup.find('div', class_='cityName cityNameShort')
    city = city.find('h1').text[1:]
    results = soup.find(id='blockDays')

    if not specific_day:
        elements = results.find_all('div', class_='main')

        for element in elements:
            dict_ = {}
            date = element.find('p', class_='date').text
            month = element.find('p', class_='month').text
            tmin = element.find('div', class_='min').text
            tmax = element.find('div', class_='max').text

            dict_['date'] = date + ' ' + month
            dict_['tmin'] = tmin
            dict_['tmax'] = tmax

            result.append(dict_)
    else:
        elements = results.find_all('table', class_='weatherDetails')

        for element in elements:
            dict_ = {}
            temperature = element.find('tr', class_='temperature')
            dict_['2:00'] = temperature.find('td', class_='p1 bR').text
            dict_['8:00'] = temperature.find('td', class_='p2 bR').text
            dict_['14:00'] = temperature.find('td', class_='p3 bR').text
            dict_['20:00'] = temperature.find('td', class_='p4').text

            result.append(dict_)
    return city, result


line = '_____________________________________________\n'
url = 'https://sinoptik.ua/'

print(line)
specific_day = False
choice = input('Показать погоду по-умолчанию? [y/n]: ')
if choice == 'n':
    city = input('Введите город: ')
    url += f'погода-{city}/'

    choice = input('Выбрать дату? [y/n]: ')
    if choice == 'y':
        date = input('Введите дату в формате "yyyy-mm-dd": ')
        url += f'{date}/'
        specific_day = True
print(line)

city, result = get_weather(url, specific_day)

print(city, '\n')
for days in result:
    for k, v in days.items():
        if specific_day:
            print(f'В {k} Температура {v}')
        else:
            print(v)
    print()
print(line)
