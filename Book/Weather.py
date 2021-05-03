import requests
from bs4 import BeautifulSoup


def Weather():
    source = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')
    soup = BeautifulSoup(source.content, "html.parser")

    table = soup.find('table', {'class': 'table_develop3'})
    data = []

    for tr in table.find_all('tr'):
        tds = list(tr.find_all('td'))
        for td in tds:
            if td.find('a'):
                point = td.find('a').text
                temp = tds[5].text
                humidity = tds[9].text

                data.append([point, temp, humidity])


    return data