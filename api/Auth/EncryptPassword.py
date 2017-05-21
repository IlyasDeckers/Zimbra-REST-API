#!flask/bin/python

from passlib.apps import custom_app_context as pwd_context

class EncryptPassword():
	
    def hash(self, password):
        return pwd_context.encrypt(password)