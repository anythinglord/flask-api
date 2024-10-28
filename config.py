import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False