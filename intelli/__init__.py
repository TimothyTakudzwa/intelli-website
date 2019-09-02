from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sslify import SSLify
from flask_mail import Mail
from flask_basicauth import BasicAuth

lm = LoginManager()

app = Flask(__name__)
sslify = SSLify(app)
db = SQLAlchemy(app)

app.config.from_object('config')
db.init_app(app)
lm.init_app(app)
app.config['BASIC_AUTH_USERNAME'] = 'intelliAdmin'
app.config['BASIC_AUTH_PASSWORD'] = 'intelli4life2020'

basic_auth = BasicAuth(app)

app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='pambenidevelopers@gmail.com',
    MAIL_PASSWORD='P@mb3n12018'
)
mail = Mail(app)
from . import models

migrate = Migrate(app, db)

from . import views, app
