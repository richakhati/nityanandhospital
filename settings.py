from flask import Flask,render_template,request,session,redirect,send_file
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from werkzeug.utils import secure_filename
from flask_ckeditor import CKEditor
from flask_mail import Mail, Message
import pandas as pd
import random

app = Flask(__name__)
mail= Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'riiichakhati18@gmail.com'
app.config['MAIL_PASSWORD'] = 'Barfi200'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

db= SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nnhospital.sqlite3"
app.config['CKEDITOR_PKG_TYPE'] = 'full-all'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
ckeditor = CKEditor(app)
