#!flask/bin/python
from run import app
from flask import request
from app.api import Response, CMD, api_routes, auth
from passlib.apps import custom_app_context as pwdhash
import ConfigParser

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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods = ['GET'])
@app.route('/<path:path>', methods = ['POST'])
@auth.login_required
def catch_all_post(path):
	post = " "
	if request.method == 'POST':
		for param in api_routes[path]["params"]:
			if not request.json.get(param):
				return Response('please provide the ' + param + ' parameter').ResponseNotFound()
			post += request.json.get(param) + " "
	return CMD().execute(api_routes[path]["command"] + post)