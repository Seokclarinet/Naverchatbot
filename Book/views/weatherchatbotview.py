from flask import Blueprint , render_template,url_for,request,flash,session,g
from werkzeug.security import generate_password_hash, check_password_hash


from datetime import datetime
from werkzeug.utils import redirect

bp= Blueprint('weatherchat',__name__,url_prefix='/weatherchat')

@bp.route('/weatherchatbot',methods=('GET',))
def weatherchat():
    return render_template('chatbot/weatherchatbot.html')