# Need this for all our forms
from flask_wtf import FlaskForm

# Fields
from wtforms import StringField, SubmitField

'''
Form with:
- First name (string)
- Submit button (submit)
'''
class MyForm(FlaskForm):
    username = StringField(label="Username")
    submit_button = SubmitField(label="Submit")