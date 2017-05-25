#!flask/bin/python
from run import app
from flask import request
from app.api import Auth, Response, CMD, api_routes, auth

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
@app.route('/api/hash', methods = ['POST'])
def new_hash():
	return Auth().update_credentials(request.json.get('username'), request.json.get('password'))