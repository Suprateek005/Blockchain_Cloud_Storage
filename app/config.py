import os
import secrets

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))
    print("SECRET_KEY :",SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SESSION_COOKIE_HTTPOLY=True
    SESSION_COOKIE_SECURE = False
    SCHEDULER_API_ENABLED = True
    # SERVER_NAME='netbug.xyz:5000'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('GMAIL_USERNAME')  # Use a custom environment variable for Gmail username
    print("MAIL_USERNAME :",MAIL_USERNAME)
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')  # Use a custom environment variable for Gmail app-specific password
    print("MAIL_PASSWORD:",MAIL_PASSWORD)
    AdminMail=os.environ.get('ADMINMAIL')
    print("AdminMail:",AdminMail)
    data_key = os.environ.get('KEY').encode() if os.environ.get('KEY') else None
    print("data_key:",data_key)
    data_iv=os.environ.get('KEY').encode() if os.environ.get('IV') else None




class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}

def get_config(mode='default'):
    return config_by_name.get(mode, DevelopmentConfig)
