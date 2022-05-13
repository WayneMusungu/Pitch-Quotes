

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    # category = SelectField('Categories', choices=[('Motivational Pitch'), ('Fashion Pitch'), ('Business Pitch'), (' Pitch')], validators=[DataRequired()])
    submit = SubmitField('Post')