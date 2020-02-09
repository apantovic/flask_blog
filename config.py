import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    MAIL_SERVER = 'smtp.live.com'
    MAIL_PORT = 587 or 995
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'alexpantex'
    MAIL_PASSWORD = 'nikolatesla91'
    ADMINS = ['alexpantex@live.com']

