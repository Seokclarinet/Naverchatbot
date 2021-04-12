from flask import Blueprint , render_template,url_for,request,flash,session,g
from werkzeug.security import generate_password_hash, check_password_hash
from Book.forms import BooknameForm
from Book.Naverbookapi import Naverbook
import json
bp = Blueprint('bookname', __name__, url_prefix='/bookname')

@bp.route('/namesearch/',methods=('POST','GET'))
def namesearch():
    form = BooknameForm()
    if request.method == 'POST' and form.validate_on_submit():
        result = Naverbook(form.subject.data)
        result = json.loads(result)

        return render_template('/bookname/namesearch.html', book_info_list=result['items'], form=form)


    return render_template('/bookname/namesearch.html',form=form)
