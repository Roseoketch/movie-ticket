import os

class Config:
    """
    General configuration parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rose:1234@localhost/watchlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    pass
class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config:The parent configuration class with general configuration settings
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    pass
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rose:password@localhost/watchlist_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rose:password@localhost/watchlist'
    DEBUG= True
class Config:
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
config_options  = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
