# Need this for all our forms
from flask_wtf import FlaskForm

# Fields
from wtforms import StringField, SubmitField, EmailField, PasswordField

# Validators
from wtforms.validators import InputRequired, EqualTo, Regexp, Length

'''
Form with:
- First name (string)
- Submit button (submit)
'''
class MyForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[
            InputRequired(),
            # Length(min=5, max=9, message="Must be between 5 and 9"),
            # Regexp('^[a-z]{6-10}$', message="Can only use lowercase characters and must be between 6 and 10 characters"),
            ]
        )
    email = EmailField(
        label="Email", 
        validators=[InputRequired()]
        )
    password = PasswordField(
        label="Password", 
        validators=[InputRequired()]
        )
    confirm_password = PasswordField(
        label="Confirm password", 
        validators=[InputRequired(), 
        EqualTo("password", message="Your passwords do not match (hi everyone!)")]
        )

    submit_button = SubmitField(label="Submit")

class LoginForm(FlaskForm):
    email = EmailField(
        label="Email", 
        validators=[InputRequired()]
        )

    password = PasswordField(
        label="Password", 
        validators=[InputRequired()]
        )
    
    submit = SubmitField(label="Submit")