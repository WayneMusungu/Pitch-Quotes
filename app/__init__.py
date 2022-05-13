from crypt import methods

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] ='52741021f2e4b45e0b912a93b895a5d862d9fd46'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'alert alert-info'



# from pitchapp import routes
from app.users.routes import users
from app.posts.routes import posts
from app.main.routes import main


app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
