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
    first_name = StringField(label="Label First name")
    submit_button = SubmitField(label="Label Submit button")