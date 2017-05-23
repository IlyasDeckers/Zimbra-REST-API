#!flask/bin/python
from flask import Flask

app = Flask(__name__)

from app.main import *

if __name__ == '__main__':
    print app.url_map
    app.run(host='0.0.0.0', port=8081, debug=True)