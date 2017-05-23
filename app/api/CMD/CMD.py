#!flask/bin/python

import subprocess

class CMD():
	def execute(self, cmd):
		return subprocess.check_output(cmd, shell=True)