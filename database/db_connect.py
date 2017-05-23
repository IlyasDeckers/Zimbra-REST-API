#!flask/bin/python

import sqlite3
from flask import g
from run import app


class DB():
	def connect(self):
	    db = getattr(g, '_database', None)
	    if db is None:
	        db = g._database = sqlite3.connect('database/_database.sqlite')
	    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()