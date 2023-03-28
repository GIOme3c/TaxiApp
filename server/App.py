from flask import Flask
from flask_cors import CORS
from datetime import timedelta
from flask_socketio import SocketIO, send

from modules import __config


app = Flask(__name__)
cors = CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024
app.config['CORS_HEADERS'] = 'Content-Type'


# See examples/csrf_protection_with_cookies.py
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_SECRET_KEY'] = __config.SECRET_KEY 
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)
app.config["JWT_COOKIE_SECURE"] = True
app.config["JWT_COOKIE_SAMESITE"] = "None"


from modules.auth import routes as auth

auth.init(app)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')