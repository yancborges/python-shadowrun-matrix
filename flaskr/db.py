from pymongo import MongoClient
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        MONGO_STR = ''
        client = MongoClient(MONGO_STR)
        g.db = client['the-matrix']

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

    


