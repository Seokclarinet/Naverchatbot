from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired

class BooknameForm(FlaskForm):
    subject = StringField('제목' , validators=[DataRequired()])



class AuthorForm(FlaskForm):
    subject = StringField('작가이름', validators=[DataRequired()])

class MovieForm(FlaskForm):
    subject = StringField('영화제목', validators=[DataRequired()])

class RankForm(FlaskForm):
    subject = StringField('년월일(예:200303)', validators=[DataRequired()])

class BuyForm(FlaskForm):
    subject1 = StringField('상품명', validators=[DataRequired()])

class ShopbuyForm(FlaskForm):
    content = TextAreaField('주소',validators=[DataRequired()])

