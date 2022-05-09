from fileinput import filename
import os
import secrets
from turtle import title
from PIL import Image
from flask import render_template,url_for,flash,redirect,request, abort
from pitchapp import app, db, bcrypt
from pitchapp.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from pitchapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



# posts = [
#     {
#         'author': 'Wayne Ortiz',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'January 12, 1924'
#     },
#       {
#         'author': 'Wo Shifu',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'December 12, 1924'
#     },
    
# ]


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            # flash('You have logged in', 'alert alert-success')
            return redirect(next_page)if next_page else redirect(url_for('home'))
            
            
        # if form.email.data == 'wayne@pitch.com' and form.password.data == '123456789':
            
        else:
            flash('Login Unsuccessful! Please check your login credentials', 'alert alert-danger')
    
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_picture', picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    
    
    i.save(picture_path)
    
    return picture_fn
    
    
@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.username.data
        db.session.commit()
        flash('Your account has been updated!', 'alert alert-success')
        
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    image_file = url_for('static', filename='profile_picture/' + current_user.image_file)
    
    return render_template('account.html', title='Account', image_file=image_file, form=form)  


@app.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been uploaded', 'alert alert-success' )
        return redirect(url_for('home'))
        
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')  


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html',title=post.title, post=post)



@app.route('/post/<int:post_id>/update')
@login_required
def update_post(post_id): 
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    form.title.data = post.title
    form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

    
