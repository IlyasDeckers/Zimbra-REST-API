#!flask/bin/python
from app.api.Response.Response import Response
import subprocess

class CMD():
	def execute(self, cmd):
		try:
			return Response("success").responseOk(subprocess.check_output(cmd, shell=True).split("\n"))
		except subprocess.CalledProcessError as e:
			return Response("error").responseInternalServerError()
