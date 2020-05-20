from pymongo import MongoClient
from flask import g
# from flask.cli import with_appcontext
from .config import url_mongo, database_name


def get_db():
    if 'db' not in g:
        client = MongoClient(url_mongo)
        g.db = client[database_name]

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
