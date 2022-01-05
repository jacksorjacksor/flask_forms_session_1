from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"]='3dcbb92fcf85643519af1816350b07d4811c3f8e4cade554'

# Database stuff




from appinav import routes