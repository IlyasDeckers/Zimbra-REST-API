#!flask/bin/python

import ConfigParser

class Config:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()  
        self.config.read('env.conf')

    def getUser(self):
        return self.config.get('USER', 'username')

    def getHash(self):
        return self.config.get('USER', 'hash')

    def updateHash(self, password):
        self.config.set('USER', 'hash', password)

        with open('env.conf', 'w') as configfile:
            self.config.write(configfile)