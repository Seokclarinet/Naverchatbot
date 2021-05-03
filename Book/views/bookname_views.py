from flask import Blueprint , render_template,url_for,request,flash,session,g
from werkzeug.security import generate_password_hash, check_password_hash
from Book.forms import BooknameForm,ShopbuyForm
from Book.Naverbookapi import Naverbook
import json
from datetime import datetime
from Book.models import Buy
from Book import db
from werkzeug.utils import redirect

bp = Blueprint('bookname', __name__, url_prefix='/bookname')

@bp.route('/namesearch/',methods=('POST','GET'))
def namesearch():
    form = BooknameForm()
    if request.method == 'POST' and form.validate_on_submit():
        result = Naverbook(form.subject.data)
        result = json.loads(result)

        return render_template('/bookname/namesearch.html', book_info_list=result['items'], form=form)


    return render_template('/bookname/namesearch.html',form=form)

@bp.route('/bookbuy',methods=('POST','GET'))
def bookbuy():
    form = ShopbuyForm()
    btitle = request.form['title']
    if request.method == "POST" and form.validate_on_submit():
        q = Buy(subject=btitle, content=form.content.data, name=form.name.data, create_date=datetime.now())
        db.session.add(q)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('/bookname/book_buy.html', form=form, title=btitle)
