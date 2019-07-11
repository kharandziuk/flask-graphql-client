from flask import Flask
from marshmallow import Schema, fields, pprint

app = Flask(__name__)


@app.route('/link', methods=['POST'])
def link():
    return '1'
