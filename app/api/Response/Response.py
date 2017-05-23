#!flask/bin/python

from flask import jsonify

class Response():
	def __init__(self, message):
		self.message = message

	def responseOk(self, result):
		status = [
			{
				"status": "ok", 
				"code": "200",
				"message": self.message,
				"result": result
			}
		]

		return jsonify(status)

	def ResponseNotFound(self):
		status = [
			{
				"status": "not found", 
				"code": "404",
				"message": self.message
			}
		]

		return jsonify(status)

	def responseInternalServerError(self):
		status = [
			{
				"status": "server error",
				"code": "500",
				"message": self.message
			}
		]

		return jsonify(status)