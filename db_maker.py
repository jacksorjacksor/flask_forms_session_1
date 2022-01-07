from appinav import db
from appinav.models import User

db.drop_all()

db.create_all()

user1 = User(username="aaa", email="a@a.a", password="a")
user2 = User(username="bbb", email="b@b.b", password="b")
user3 = User(username="ccc", email="c@c.c", password="c")

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

db.session.commit()