#!flask/bin/python

from api import CMD

class Mailbox():

	def __init__(self):
		self.test = 'test'

	def createMailbox(self, request):
		return CMD().execute(request.json.get("cmd"))

	def update(self):
		pass

	def delete():
		pass