from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0960922431deb454f72e762abc4b5986'

posts = [
    {
        'author': 'Charles Stephen',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted': '20-Jan-2021'
    },
    {
        'author': 'Stephen Charles',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': '20-Jan-2021'
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')

    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)
