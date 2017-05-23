#!flask/bin/python

'''

Main Routes for the Zimbra API

'''
from run import app
from flask import request
from api import *
from database.db_connect import DB
from passlib.apps import custom_app_context as pwdhash
from flask.ext.httpauth import HTTPBasicAuth
import ConfigParser, subprocess

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
	config = ConfigParser.ConfigParser()
	config.read('.env')
	pwd = config.get('USER', 'password')
	if not username or not pwdhash.verify(password, pwd):
		return False
 	return True

@app.route('/api')
@auth.login_required
def Home():
	return Response('Welcome').responseOk()

# Update password	
@app.route('/api/hash', methods = ['POST'])
def new_hash():
	config = ConfigParser.ConfigParser()  
	config.read('.env')
	if not config.get('USER', 'password'):
		config.set('USER', 'password', pwdhash.encrypt(request.json.get('password')))
		config.set('USER', 'username', request.json.get('username'))
		with open('.env', 'w') as configfile:
			config.write(configfile)
		msg = 'Password has been updated'
	else:
		msg = 'Auth token already present'
	return Response(msg).responseOk()

# Create Mailbox
@app.route('/api/domain/create', methods = ['POST'])
@auth.login_required
def create_domain():
	if request.json.get('domain'):
		try:
			result = CMD().execute("zmprov createDomain " + request.json.get('domain'))
			return Response("success").responseOk(result)
		except subprocess.CalledProcessError as e:
			return Response("error").responseInternalServerError()
	return Response('please provide a domain').ResponseNotFound()

# Get all users accounts
@app.route('/api/accounts/get', methods = ['POST'])
@auth.login_required
def get_accounts():
	try:
		result = CMD().execute("zmprov -l GetAllAccounts " + request.json.get('domain'))
		return Response("success").responseOk(result)
	except subprocess.CalledProcessError as e:
		return Response("error").responseInternalServerError()

# Create a mailbox
@app.route('/api/mailbox/create', methods = ['POST'])
@auth.login_required
def create_mailbox():
	pass
# Update Mailbox
@app.route('/api/mailbox/update', methods = ['POST'])
@auth.login_required
def update_mailbox():
	pass

# Delete Mailbox
@app.route('/api/mailbox/delete', methods = ['POST'])
@auth.login_required
def delete_mailbox():
	pass

