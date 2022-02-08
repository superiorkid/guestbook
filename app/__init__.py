from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from faker import Faker

app = Flask(__name__)
app.config.from_object(Config)
mongodb_client = PyMongo(app)
db = mongodb_client.db
fake = Faker()

from app import routes