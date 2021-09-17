from enum import unique
import json
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, form
from werkzeug import security
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from wtforms.widgets.core import Input
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from Security.Control.IPControl import Hammer

app = Flask(__name__)
app.config['SECRET_KEY'] = "Thisissupposedtobescret!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Musel/Desktop/Programing/Project/AutoRIP2-adjusting/Panel/database.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class LoginForm(FlaskForm):
    username = StringField('',validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('',validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('', render_kw={'ref': 'RememberBoxArea'})

class RegisterForm(FlaskForm):
    email = StringField('', validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)])
    username = StringField('', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('', validators=[InputRequired(), Length(min=8, max=80)])

@app.route("/")
def index():
    if(Hammer() == True):
        return render_template("Forbidden.html", text="Forbidden 403")
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    if(Hammer() == True):
        return render_template("Forbidden.html", text="Forbidden 403")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
        return "<h1>Invalid username or password</h1>"
        #return "<h1>" + form.username.data + ' ' + form.password.data + '</h1>'
    return render_template("signin.html", form=form)

@app.route("/signup", methods=["GET","POST"])
def signup():
    if(Hammer() == True):
        return render_template("Forbidden.html", text="Forbidden 403")
    form = RegisterForm()
    if form.validate_on_submit():
        hash_password = generate_password_hash(form.password.data, method="sha256")
        new_user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(new_user)
        db.session.commit()
        return "<h1>New User Has Been Created!</h1>"
        #return "<h1>" + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template("signup.html", form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    if(Hammer() == True):
        return render_template("Forbidden.html", text="Forbidden 403")
    return render_template("dashboard.html", name=current_user.username)

if __name__ == '__main__':
    app.run(debug=True)