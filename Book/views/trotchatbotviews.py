from flask import Blueprint , render_template,url_for,request,flash,session,g
from werkzeug.security import generate_password_hash, check_password_hash


from datetime import datetime
from werkzeug.utils import redirect

bp= Blueprint('trotchat',__name__,url_prefix='/trotchat')

@bp.route('/trotchatbot',methods=('GET',))
def trotchat():
    return render_template('chatbot/trotchatbot.html')