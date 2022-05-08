
from crypt import methods
from flask import Flask,render_template,url_for,flash,redirect
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

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'alert alert-success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'wayne@pitch.com' and form.password.data == '123456789':
            flash('You have been logged in', 'alert alert-success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check your login credentials', 'alert alert-danger')
    
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)