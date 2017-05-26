#!flask/bin/python
from run import app
from flask import request
from app.api import Auth, Response, CMD, api_routes, auth

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods = ['GET', 'POST'])
@auth.login_required
def routes(path):
	post = " "
	if request.method == 'POST':
		for param in api_routes[path]["params"]:
			if not request.json.get(param):
				return Response("error").badRequest('please provide the ' + param + ' parameter')
			post += request.json.get(param) + " "
	return CMD().execute(api_routes[path]["command"] + post)
@app.route('/api/hash', methods = ['POST'])
def new_hash():
	return Auth().update_credentials(request.json.get('username'), request.json.get('password'))