from flask import Flask
from flask_mail import Mail
from .config import Config
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
from app import views
