from flask import Blueprint , render_template ,request, url_for
from werkzeug.utils import redirect
from datetime import datetime
import json
from Book.forms import BuyForm,ShopbuyForm
from Book.NaverShopping import Navershop
from Book import db
from Book.models import Buy

bp = bp = Blueprint('shopping', __name__, url_prefix='/shopping')

@bp.route('/search/',methods=('POST','GET'))
def buysearch():
    form = BuyForm()
    if request.method == 'POST' and form.validate_on_submit():
        result = Navershop(form.subject1.data)
        result = json.loads(result)
        return render_template('shopping.html', shop_info_list=result['items'], form=form)
    return render_template('shopping.html', form=form)

@bp.route('/buy',methods=('POST','GET'))
def buy():
    form = ShopbuyForm()
    stitle=request.form['title']
    slprice=request.form['lprice']
    if request.method == "POST" and form.validate_on_submit():
        q = Buy(subject=stitle, content=form.content.data,price=slprice, create_date=datetime.now())
        db.session.add(q)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('shop_buy.html',form=form,title=stitle,lprice=slprice)