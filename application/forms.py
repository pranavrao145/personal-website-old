from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactMeForm(FlaskForm):
    name = StringField("Enter your name:", validators=[DataRequired()])
    email = StringField("Enter your email:", validators=[DataRequired(), Email()])
    message = TextAreaField("Type your message here:", validators=[DataRequired()])
    submit = SubmitField("Submit")
