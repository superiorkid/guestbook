from flask import Flask
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)
mongodb_client = PyMongo(app)
db = mongodb_client.db

from app import routes