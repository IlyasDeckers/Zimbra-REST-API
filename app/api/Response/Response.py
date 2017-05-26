#!flask/bin/python

from flask import jsonify
import json

class Response():
	def __init__(self, message):
		self.message = message

	def success(self, result):
		status = [
			{
				"status": "ok", 
				"code": "200",
				"message": self.message,
				"result": result
			}
		]

		return jsonify(status)
	
	def badRequest(self, result):
		status = [
			{
				"status": "bad request", 
				"code": "400",
				"message": self.message,
				"result": result
			}
		]

		return jsonify(status)

	def notFound(self):
		status = [
			{
				"status": "not found", 
				"code": "404",
				"message": self.message
			}
		]

		return jsonify(status)

	def internalServerError(self):
		status = [
			{
				"status": "server error",
				"code": "500",
				"message": self.message
			}
		]

		return jsonify(status)