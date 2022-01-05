from flask import render_template
from appinav import app
from appinav.forms import MyForm


@app.route("/", methods=["GET", "POST"])
def home():
    my_amazing_form = MyForm()

    if my_amazing_form.is_submitted():
        new_var = my_amazing_form.first_name.data
    else:
        new_var=None

    return render_template("home.html", my_amazing_form=my_amazing_form, new_var=new_var)
