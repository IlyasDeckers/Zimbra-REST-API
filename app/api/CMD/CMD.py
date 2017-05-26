#!flask/bin/python
from app.api.Response.Response import Response
import subprocess

class CMD():
	def execute(self, cmd):
		try:
			response = subprocess.check_output(cmd, shell=True)
			result = [x for x in response.split("\n") if x]
			return Response("success").success(result)
		except subprocess.CalledProcessError as e:
			return Response("error").internalServerError()
