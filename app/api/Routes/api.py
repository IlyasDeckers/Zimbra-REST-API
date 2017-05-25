#!flask/bin/python
from flask import jsonify
import json

with open('app/routes/api.json') as routes:    
	api_routes = json.load(routes)