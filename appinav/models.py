from appinav import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    hashed_password = db.Column(db.String(120))
    
    @property
    def password(self):
        raise AttributeError('Password is not readable.')

    @password.setter
    def password(self,password):
        self.hashed_password=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))