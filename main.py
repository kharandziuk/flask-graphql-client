from flask import Flask, jsonify, request
from data_access import get_data
from marshmallow import Schema, fields, ValidationError, utils

DATE_FORMAT = '%Y-%m-%d'

app = Flask(__name__)

class LinkSchema(Schema):
    amount = fields.Number(required=True)
    payment_reference = fields.Str(required=True)
    # FIXME: use DateField
    payment_date = fields.Date(required=True)

link_schema = LinkSchema(unknown=utils.RAISE)

def is_reconcile(payable, searched):
    # FIXME: it's just a set of possible check I didn't finetune it
    if abs(payable['amount'] - searched['amount']) < 1:
        return True
    if payable['referenceId'].lower() == searched['payment_reference'].lower():
        return True
    if payable['dateOccurred'] == searched['payment_date'].strftime(DATE_FORMAT):
        return True
    return False

def search(data, searched):
    return [entry for entry in get_data() if is_reconcile(entry, searched)]



@app.route('/link', methods=['POST'])
def link():
    json_input = request.get_json()
    try:
        link_input = link_schema.load(json_input)
    except ValidationError as err:
        return jsonify(err.messages), 422
    result = search(get_data(), link_input)
    return jsonify(result)
