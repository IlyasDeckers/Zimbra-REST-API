#!flask/bin/python

'''

Main Routes for the Zimbra API

'''

from run import app
from flask import request
from api import *

@app.route('/api')
def Home():
    user = Config()
    return 'Welcome, ' + user.getUser()

@app.route('/api/hash', methods = ['POST'])
def new_hash():
    Config().updateHash(EncryptPassword().hash(request.json.get('password')))
    return 'Password has been updated.'

# Create Mailbox
@app.route('/api/mailbox/create', methods = ['POST'])
def create_mailbox():
    return Mailbox().createMailbox(request)

# Update Mailbox
@app.route('/api/mailbox/update', methods = ['POST'])
def update_mailbox():
    pass

# Delete Mailbox
@app.route('/api/mailbox/delete', methods = ['POST'])
def delete_mailbox():
    pass

