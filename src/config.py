import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Development(object):
    """Development environment configuration.""" 
    DEBUG = True
    TESTING = False
    
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'rpi.db')

class Production(object):
    """Production environment configuration."""
    DEBUG = False
    TESTING = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prod.db')


class Testing(object):
    """Testing environment configuration."""
    DEBUG = False
    TESTING = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing,
}