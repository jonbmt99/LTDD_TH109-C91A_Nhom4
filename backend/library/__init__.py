import smtplib

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
bcrypt = Bcrypt(app)
app.config.from_object('config')
app.config['DEFAULT_PARSERS'] = [
    'flask.ext.api.parsers.JSONParser',
    'flask.ext.api.parsers.URLEncodedParser',
    'flask.ext.api.parsers.FormParser',
    'flask.ext.api.parsers.MultiPartParser'
]
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
from library import controllers


