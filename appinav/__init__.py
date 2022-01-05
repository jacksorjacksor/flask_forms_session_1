from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"]='3dcbb92fcf85643519af1816350b07d4811c3f8e4cade554'

# Database stuff
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir,'my_db.db')}"

# Creates instance of the database
db = SQLAlchemy(app)

from appinav import routes