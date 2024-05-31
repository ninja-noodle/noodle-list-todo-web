from decouple import config
from flask import Flask, render_template, redirect, url_for, request, abort
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

# ================== Flask app config ====================== #
app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')
Bootstrap5(app)

# ================== Essential setup ====================== #
login_manager = LoginManager()
login_manager.init_app(app)


# ================== Initializing database ====================== #
app.config['SQLALCHEMY_DATABASE_URI'] = config('DB_URI')
db = SQLAlchemy()
db.init_app(app)

# ================== Database table template ====================== #


class ToDoList(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates='posts')
    task = db.Column(db.String(250), unique=True, nullable=False)
    date = db.Column(db.String(250), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    todolist = relationship("ToDoList", back_populates="user")


# ================== Creating database ====================== #
with app.app_context():
    db.create_all()

# ================== App routes ====================== #


@login_manager.user_loader
@app.route('/')
def main():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
