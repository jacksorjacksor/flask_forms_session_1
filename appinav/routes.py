from flask import render_template, redirect, url_for, flash
from appinav import app, db
from appinav.forms import MyForm, LoginForm
from appinav.models import User
from flask_login import login_user, logout_user


@app.route("/", methods=["GET", "POST"])
def home():
    my_amazing_form = MyForm()

    if my_amazing_form.validate_on_submit():
        new_var = my_amazing_form.username.data

        new_user = User(username=my_amazing_form.username.data,email=my_amazing_form.email.data,password=my_amazing_form.password.data)

        db.session.add(new_user)
        db.session.commit()
        flash(f"This user has now been added! {my_amazing_form.username.data}")
    else:
        new_var=None

    # All users
    list_of_users = User.query.all()

    return render_template("home.html", my_amazing_form=my_amazing_form, new_var=new_var, list_of_users=list_of_users)

# LOGIN DETAILS

@app.route("/login", methods=["GET","POST"])
def login():
    my_login_form = LoginForm()
    
    if my_login_form.validate_on_submit():
        user_to_login = User.query.filter_by(email=my_login_form.email.data).first()
        if user_to_login:
            login_user(user_to_login)
            flash(f"FLASH: You have logged in")
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login_error'))

    return render_template("login.html", my_login_form=my_login_form)

@app.route("/error-page")
def login_error():
    return "Things did not go well when logging in"

@app.route("/logout")
def logout():
    logout_user()
    flash(f"FLASH: You have logged out")
    return redirect(url_for('home'))


##### THE FOUR QUERIES OF THE APOCALYPSE
'''
.all()  # Returns a list

.first() # Returns a class object

.order_by() # Returns a list

.filter_by() # Returns a list
'''

@app.route("/all")
def all():
    list_of_users = User.query.all()
    return render_template("all.html",list_of_users=list_of_users)

@app.route("/first")
def first():
    one_user = User.query.first()
    return render_template("first.html",one_user=one_user)

@app.route("/order_by")
def order_by():
    list_of_users_ordered_by_pk_desc = User.query.order_by(User.id.desc())
    list_of_users_ordered_by_pk_asc = User.query.order_by(User.id.asc())
    return render_template("ordered.html",list_of_users_ordered_by_pk_desc=list_of_users_ordered_by_pk_desc,
    list_of_users_ordered_by_pk_asc=list_of_users_ordered_by_pk_asc)

@app.route("/filter_by/<string:my_variable>")
def filter_by(my_variable):
    user = User.query.filter_by(username=my_variable).first()
    return render_template("filtered.html", user=user)


###########################################################################

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

###########################################################################

