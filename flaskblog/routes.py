from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post



posts = [
    {
        'author': 'John Wich',
        'title': 'My dog', 
        'content': 'my dog',
        'date_posted': 'April 1, 2020'
    },
    {
        'author': 'Jack Sparrow',
        'title': 'Black Pearl',
        'content': 'my ship',
        'date_posted': 'July 1, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "password":
            flash(" You are logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessfull. Please check username and password.", 'danger')
    return render_template('login.html', title='Login', form=form)
