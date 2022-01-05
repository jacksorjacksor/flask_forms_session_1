from appinav import db
from appinav.models import User

db.drop_all()

db.create_all()

user1 = User(username="111")
user2 = User(username="222")
user3 = User(username="333")

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

db.session.commit()