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





    





    
