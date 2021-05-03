from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import config


naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


app = Flask(__name__)
app.config.from_object(config)
app.debug = True

# DRM 데이터베이스 초기화
db.init_app(app)

migrate.init_app(app,db)

from .views import author_views, movie_views, shopping_views, chatbotviews, bookname_views, \
    main_views,webhook_views,moviehook_views,moviechatviews,weatherchatbotview,trotchatbotviews,\
    dialogflowapi_views,helpbot_views
app.register_blueprint(author_views.bp)
app.register_blueprint(movie_views.bp)
app.register_blueprint(shopping_views.bp)
app.register_blueprint(chatbotviews.bp)
app.register_blueprint(bookname_views.bp)
app.register_blueprint(main_views.bp)
app.register_blueprint(webhook_views.bp)
app.register_blueprint(moviehook_views.bp)
app.register_blueprint(moviechatviews.bp)
app.register_blueprint(weatherchatbotview.bp)
app.register_blueprint(trotchatbotviews.bp)
app.register_blueprint(dialogflowapi_views.bp)
app.register_blueprint(helpbot_views.bp)
#필터등록
from .filter import Shortword
app.jinja_env.filters['shortword'] = Shortword


