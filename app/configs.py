import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://app_user:app_password@localhost:5432/flask_practice"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
