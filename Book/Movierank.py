# 날짜 변경
import requests
from bs4 import BeautifulSoup
import urllib.request

def movierank(date):
    url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20'
    encText = urllib.parse.quote(date)
    tit_lst=[]




    html = requests.get(url+ encText)
    soup = BeautifulSoup(html.text, "html.parser")

        # 해당 페이지(날짜별 페이지)에서 영화 제목 추출
    tit5_tag = soup.find_all('div',class_='tit3')

    for num in range(len(tit5_tag)):

            title = tit5_tag[num].find('a').text
            tit_lst.append(title)
    return tit_lst