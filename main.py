from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError, utils

app = Flask(__name__)

class LinkSchema(Schema):
    amount = fields.Number(required=True)
    payment_reference = fields.Str(required=True)
    # FIXME: use DateField
    payment_date = fields.Str(required=True)

link_schema = LinkSchema(unknown=utils.RAISE)


@app.route('/link', methods=['POST'])
def link():
    json_data = request.get_json()
    print(json_data)
    try:
        data = link_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    return jsonify(data)
