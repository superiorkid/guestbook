from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from faker import Faker
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.config.from_object(Config)
mongodb_client = PyMongo(app)
db = mongodb_client.db
fake = Faker()
bootstrap = Bootstrap4(app)

from app import routes