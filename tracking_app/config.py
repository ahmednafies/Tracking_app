# -*- coding: utf-8 -*-
"""Configuration Module
Module handles the configuration of different environments (Dev, Test and Prod)
"""
import os

import dj_database_url
from dotenv import load_dotenv


class Config:
    DEBUG = True
    HEROKU = os.getenv("HEROKU")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(BASE_DIR, ".env"))
    SECRET_KEY = os.environ["SECRET_KEY"]
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".ngrok.io"]
    CORS_ORIGIN_WHITELIST = ("localhost:8080",)


class Dev(Config):
    CORS_ORIGIN_ALLOW_ALL = True

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "HOST": "db",
            "PORT": 5432,  # default postgres port
        }
    }


class Test(Config):
    DEBUG = False

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "circleci_test",
            "USER": "circleci",
            "HOST": "localhost",
            "PORT": 5432,
        }
    }


class Staging(Config):
    DEBUG = False
    DATABASES = {}
    DATABASES["default"] = dj_database_url.config(conn_max_age=600)
    ALLOWED_HOSTS = ["tracking-app-staging.herokuapp.com"]


class Prod(Config):
    DEBUG = False
    DATABASES = {}
    DATABASES["default"] = dj_database_url.config(conn_max_age=600)
    ALLOWED_HOSTS = ["tracking-app.herokuapp.com"]


def get_config():
    env = os.environ["ENV"]

    if env == "PROD":
        return Prod()

    if env == "TEST":
        return Test()

    if env == "STAGING":
        return Staging()

    return Dev()


CONFIG = get_config()
