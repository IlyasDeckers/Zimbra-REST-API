#!flask/bin/python

from app.database.db_connect import DB

conn = DB().connect()
conn.execute('CREATE TABLE users (name TEXT, password TEXT)')
conn.close()

print "Install successful"