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
    subject = StringField('상품명', validators=[DataRequired()])

class ShopbuyForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired()])
    content = TextAreaField('주소',validators=[DataRequired()])


class HelpbotForm(FlaskForm):
    subject = StringField('궁금한 기능을 입력해주세요.' , validators=[DataRequired()])
