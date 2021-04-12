from flask import Blueprint , render_template,url_for,request,flash,session,g
import json
from Book.forms import MovieForm,RankForm
from Book.Movie import Movie
from Book.Movierank import movierank

bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/info/',methods=('POST','GET'))
def movieinfo():
    form = MovieForm()
    if request.method == 'POST' and form.validate_on_submit():
        result = Movie(form.subject.data)
        result = json.loads(result)
        return render_template('movie.html', book_info_list=result['items'], form=form)
    return render_template('movie.html', form=form)



@bp.route('/rank/',methods=('POST','GET'))
def movieranking():
    form = RankForm()
    if request.method == 'POST' and form.validate_on_submit():
        result = movierank(form.subject.data)
        return render_template('movierank.html', rank_list=result, form=form)
    return render_template('movierank.html', form=form)