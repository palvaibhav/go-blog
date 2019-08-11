from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")


class CommentForm(FlaskForm):
    comment_body = TextAreaField("Write a comment :-", validators=[DataRequired()])
    submit = SubmitField("Add")
