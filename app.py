from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
import models
import os

from api.user import user


DEBUG = True
PORT = 8000

login_manager = LoginManager()


app = Flask(__name__, static_url_path="", static_folder="static")

app.secret_key = 'RLAKJDRANDOM STRING'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


CORS(dogs_api, origins=["http://localhost:3000", "https://flask-react-project2.herokuapp.com/"], supports_credentials=True)

app.register_blueprint(user)


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return 'hi'

if 'ON_HEROKU' in os.environ:
    print('hitting ')
    models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)



