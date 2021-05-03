from flask import Blueprint,request
from Book.Movie import Movie
from Book.Movierank import movierank
import json
from Book import db
from Book.models import moviehook
from datetime import datetime

bp= Blueprint('moviehook',__name__,url_prefix='/moviehook')

@bp.route('/moviechat',methods=['GET','POST'])
def moviechat():
    req= request.get_json(force=True)
    intent = req['queryResult']['action']

    if intent == 'Moviename.Moviename-custom':
        movietitle = req['queryResult']['queryText']  # dialog의 채팅내용
        result = Movie(movietitle)  # 네이버 api를 활용 책 정보획득
        moviedata = json.loads(result)  # 책정보를 json으로 변환
        movieresult = moviedata['items'][0]  # 맨처음 들어온 책 정보를 획득
        senddata = '영화의 제목은' + movieresult['title'] + '입니다.' + '영화의 감독은' + movieresult['director'] + '입니다.' + '평점은' + \
                   movieresult['userRating'] + '입니다.'+ '주연은'+movieresult['actor']+'입니다.'
        mmodel = moviehook(intentid=intent, querytext=movietitle, senddata=senddata, create_date=datetime.now())
        db.session.add(mmodel)
        db.session.commit()

    elif intent == 'movierank.movierank-custom':
        movietitle = req['queryResult']['queryText']  # dialog의 채팅내용
        result = movierank(movietitle)  # 네이버 api를 활용 책 정보획득
        senddata = ''
        i=0

        for temp in result:
            i+=1
            senddata= senddata + str(i) + '위'+ temp + '|'
            if i==5:
                break
        mrodel = moviehook(intentid=intent, querytext=movietitle, senddata=senddata, create_date=datetime.now())
        db.session.add(mrodel)
        db.session.commit()

    return {'fulfillmentText': senddata}