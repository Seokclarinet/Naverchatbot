from flask import Blueprint , render_template,url_for,request,flash,session,g
from werkzeug.security import generate_password_hash, check_password_hash


from datetime import datetime
from werkzeug.utils import redirect

bp= Blueprint('moviechat',__name__,url_prefix='/moviechat')

@bp.route('/moviechatbot',methods=('GET',))
def moviechat():
    return render_template('chatbot/moviechatbot.html')