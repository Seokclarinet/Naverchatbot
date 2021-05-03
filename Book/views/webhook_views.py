from flask import Blueprint,request
from Book.Naverbookapi import Naverbook
from Book.Naverbookapiauth import Naverbookauth
from Book.Weather import Weather
import json
from Book import db
from Book.models import webhook
from datetime import datetime
from Book.models import Vote

bp= Blueprint('webhook',__name__,url_prefix='/webhook')

@bp.route('/book',methods=['GET','POST'])
def chatbot():
    req= request.get_json(force=True)
    intent = req['queryResult']['action']

    if intent == 'searchtitle.searchtitle-custom':
        booktitle = req['queryResult']['queryText']  # dialog의 채팅내용
        result = Naverbook(booktitle)  # 네이버 api를 활용 책 정보획득
        bookdata = json.loads(result)  # 책정보를 json으로 변환
        bookresult = bookdata['items'][0]  # 맨처음 들어온 책 정보를 획득
        senddata = '책의 제목은' + bookresult['title'] + '입니다.' + '책의 저자는' + bookresult['author'] + '입니다.' + '최저가는' + \
                   bookresult['discount'] + '입니다.'
        imodel = webhook(intentid=intent,querytext=booktitle,senddata=senddata,create_date=datetime.now())
        db.session.add(imodel)
        db.session.commit()

    elif intent == 'searcharthor.searcharthor-custom':
        booktitle = req['queryResult']['queryText']  # dialog의 채팅내용
        result = Naverbookauth(booktitle)  # 네이버 api를 활용 책 정보획득
        bookdata = json.loads(result)  # 책정보를 json으로 변환
        bookresult = bookdata['items'][0]  # 맨처음 들어온 책 정보를 획득
        senddata =  '책의 저자:' + bookresult['author'] + '가.' + '쓴 책의 제목은:' + bookresult['title'] + '이고' +'책의 내용은:' +bookresult['description'] + '입니다.'+ '책의 가격은'+bookresult['price'] + '원 입니다.'


    return {'fulfillmentText': senddata}


@bp.route('/weather' , methods=['GET','POST'])
def weatherbot():
    req = request.get_json(force=True)
    print(req)
    intent = req['queryResult']['action']
    print(intent)

    if intent == 'weatherchatbot.weatherchatbot-custom':
        city = req['queryResult']['queryText']
        print(city)
        resultdata = Weather()



        for temp in resultdata:

            if temp[0] == city:  #채팅의 지역과 기상청의 지역이 같으면
                senddata = city+'의 기온은'+temp[1]+'입니다.'
                return {'fulfillmentText': senddata}
                break

        return {'fulfillmentText': "지역명을 확인해 주세요"}

@bp.route('/vote' , methods=['GET','POST'])
def votebot():
    req = request.get_json(force=True)
    intent = req['queryResult']['action']
    if intent == 'vote.vote-custom':
        q=Vote.query.filter(Vote.name=='이찬원').first()
        q.count +=1
        db.session.commit()
    elif intent == 'vote.vote-custom-2':
        q=Vote.query.filter(Vote.name=='임영웅').first()
        q.count +=1
        db.session.commit()
    elif intent == 'vote.vote-custom-3':
        q=Vote.query.filter(Vote.name=='영탁').first()
        q.count +=1
        db.session.commit()
    elif intent == 'vote.vote-custom-4':
        q=Vote.query.filter(Vote.name=='정동원').first()
        q.count +=1
        db.session.commit()
    elif intent == 'vote.vote-custom-5':
        q=Vote.query.filter(Vote.name=='김호중').first()
        q.count +=1
        db.session.commit()
    elif intent == 'vote.vote-custom-6':
        q=Vote.query.filter(Vote.name=='김희재').first()
        q.count +=1
        db.session.commit()
    elif intent == 'vote.vote-custom-7':
        q=Vote.query.filter(Vote.name=='장민호').first()
        q.count +=1
        db.session.commit()

    result=[]
    qr = Vote.query.all()

    for temp in qr:
        result.append(temp.name)
        result.append(temp.count)

    return {'fulfillmentText': "투표가 완료되었습니다. 투표결과는 "+str(result)+'입니다'}
