import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'sandbox.smtp.mailtrap.io')
    MAIL_PORT = os.environ.get('MAIL_PORT', '2525')
    MAIL_USERNAME = os.environ.get('8d2aa123f58df6')
    MAIL_PASSWORD = os.environ.get('4926aa576a89e7')
    
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
