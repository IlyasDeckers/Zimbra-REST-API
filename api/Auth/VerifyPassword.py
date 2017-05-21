#!flask/bin/python
from passlib.apps import custom_app_context as pwd_context

class VerifyPassword():

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)