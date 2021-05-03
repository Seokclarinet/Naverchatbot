from flask import Blueprint , render_template,url_for,request,flash,session,g
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint
from Book.dialogflowapi import dialogflow_chat
from datetime import datetime
from werkzeug.utils import redirect
from flask import Blueprint,request
import json
from Book import db
from Book.models import webhook
from flask import Blueprint
from Book.dialogflowapi import dialogflow_chat
from Book.forms import HelpbotForm

bp= Blueprint('helpbot',__name__,url_prefix='/helpbot')

@bp.route('/helpbot',methods=('POST','GET'))
def helpchat():
    form = HelpbotForm()
    if request.method == 'POST' and form.validate_on_submit():
        result = dialogflow_chat(form.subject.data)
        intent=result.query_result.intent.display_name
        if intent =='Bookname':
            return redirect(url_for('bookname.namesearch'))
        elif intent =='author':
            return redirect(url_for('author.authorsearch'))
        elif intent =='moviename':
            return redirect(url_for('movie.movieinfo'))
        elif intent =='movierank':
            return redirect(url_for('movie.movieranking'))
        elif intent =='shopping':
            return redirect(url_for('shopping.buysearch'))



    return render_template('chatbot/helpbot.html',form=form)


