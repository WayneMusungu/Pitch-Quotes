from flask import render_template,url_for,flash,redirect
from pitchapp import app, db, bcrypt
from pitchapp.forms import RegistrationForm, LoginForm
from pitchapp.models import User, Post



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
        hashed_pasword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pasword)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account for {form.username.data} has been created you can now Login!', 'alert alert-success')
        return redirect(url_for('login'))
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