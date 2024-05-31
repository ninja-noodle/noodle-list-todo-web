from decouple import config
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy


# ================== Flask app config ====================== #
app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')
Bootstrap5(app)


# ====== DATABASE CONNECTION =======
app.config['SQLALCHEMY_DATABASE_URI'] = config('DB_URI')
db = SQLAlchemy()
db.init_app(app)

