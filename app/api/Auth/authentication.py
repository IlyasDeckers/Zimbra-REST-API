#!flask/bin/python
from passlib.apps import custom_app_context as pwd_context
from passlib.apps import custom_app_context as pwdhash
from flask.ext.httpauth import HTTPBasicAuth
import ConfigParser

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
	config = ConfigParser.ConfigParser()
	config.read('.env')
	if not username or not pwdhash.verify(password, config.get('USER', 'password')):
		return False
 	return True  