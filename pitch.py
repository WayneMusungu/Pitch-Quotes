from turtle import title
from flask import Flask,render_template,url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] ='52741021f2e4b45e0b912a93b895a5d862d9fd46'

posts = [
    {
        'author': 'Wayne Ortiz',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 12, 1924'
    },
      {
        'author': 'Wo Shifu',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 12, 1924'
    },
    
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/rlogin")
def register():
    form = LoginForm()
    return render_template('register.html', title='LLogin', form=form)

if __name__ == '__main__':
    app.run(debug=True)