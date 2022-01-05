from flask import render_template
from appinav import app, db
from appinav.forms import MyForm
from appinav.models import User


# @app.route("/", methods=["GET", "POST"])
# def home():
#     my_amazing_form = MyForm()

#     if my_amazing_form.is_submitted():
#         new_var = my_amazing_form.username.data

#         new_user = User(username=my_amazing_form.username.data)

#         db.session.add(new_user)
#         db.session.commit()
#     else:
#         new_var=None

#     # All users
#     list_of_users = User.query.all()

#     return render_template("home.html", my_amazing_form=my_amazing_form, new_var=new_var, list_of_users=list_of_users)

##### THE FOUR QUERIES OF THE APOCALYPSE
'''
.all()  # Returns a list

.first() # Returns a class object

.order_by() # Returns a list

.filter_by() # Returns a list
'''

@app.route("/")
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