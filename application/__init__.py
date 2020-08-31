from flask import Flask
from flask_mail import Mail
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config["MAIL_SERVER"] = 'smtp.googlemail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get('EMAIL_USER')
app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PASS')
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get('EMAIL_USER')

mail = Mail(app)

from . import routes
