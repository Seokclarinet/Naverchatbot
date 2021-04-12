from flask import Blueprint , render_template,url_for,request,flash,session,g
from werkzeug.security import generate_password_hash, check_password_hash
from Book.forms import AuthorForm
from Book.Naverbookapiauth import Naverbookauth
import json
bp = Blueprint('author', __name__, url_prefix='/author')

@bp.route('/authorsearch/',methods=('POST','GET'))
def authorsearch():
    form= AuthorForm()
    if request.method == 'POST' and form.validate_on_submit():
        result = Naverbookauth(form.subject.data)
        result = json.loads(result)

        return render_template('/author/authorsearch.html',book_info_list=result['items'],  form=form)
    return render_template('/author/authorsearch.html',form=form)