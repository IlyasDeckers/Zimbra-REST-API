#!flask/bin/python
from run import app
from flask import request, jsonify
from app.api import *
from passlib.apps import custom_app_context as pwdhash
from flask.ext.httpauth import HTTPBasicAuth
import ConfigParser, subprocess

auth = HTTPBasicAuth()

'''
	Functions
'''

#
# Execute command in shell
#
def execute(cmd):
	try:
		# CMD().execute(module, cmd, args)
		return Response("success").responseOk(subprocess.check_output(cmd, shell=True).split("\n"))
	except subprocess.CalledProcessError as e:
		return Response("error").responseInternalServerError()
	
#
# Verify password
#
@auth.verify_password
def verify_password(username, password):
	config = ConfigParser.ConfigParser()
	config.read('.env')
	if not username or not pwdhash.verify(password, config.get('USER', 'password')):
		return False
 	return True

'''
	Routes
	
	GET		/api
	POST	/api/hash
	POST	/api/domain
	POST 	/api/accounts
	POST	/api/accounts/create
'''
@app.route('/api')
@auth.login_required
def Home():
	config = ConfigParser.ConfigParser()
	config.read('.env')
	return Response('success').responseOk("Welcome, " + config.get('USER', 'username'))

# Create Mailbox
@app.route('/api/domain/create', methods = ['POST'])
@auth.login_required
def create_domain():
	if request.json.get('domain'):
		return execute("zmprov createDomain " + request.json.get('domain'))
	return Response('please provide a domain').ResponseNotFound()

# Get all users accounts
@app.route('/api/accounts', methods = ['POST'])
@auth.login_required
def get_accounts():
	domain = ""	
	if request.json.get('domain'):
		domain = request.json.get('domain')
	return execute("zmprov -l GetAllAccounts " + domain)

# Create a mailbox
@app.route('/api/accounts/create', methods = ['POST'])
@auth.login_required
def create_mailbox():	
	return execute("zmprov createAccount " + request.json.get('domain') + " password")

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

# Update API password	
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
	return Response("success").responseOk(msg)