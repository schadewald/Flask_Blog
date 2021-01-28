from flask import Flask, render_template, url_for
app = Flask(__name__)

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
