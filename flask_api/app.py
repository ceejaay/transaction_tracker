from flask import Flask, jsonify, request
from db import get_merchants, get_merchant_by_id, update_merchant, insert_merchant, delete_merchant
app = Flask(__name__)

@app.route('/merchants/', methods=['POST'])
def add_merchant():
    merchant = request.get_json()
    return jsonify(insert_merchant(merchant))

@app.route('/merchants/<int:index>', methods=['PUT'])
def update_merchant(index):
    return {"merchant": "updated", "id": index}, 200

@app.route('/merchants/<int:index>', methods=['DELETE'])
def delete_one_merchant(index):
    return jsonify(delete_merchant(index))

@app.route('/', methods=['GET'])
def all_merchants():
    return jsonify(get_merchants())

@app.route('/merchants/<int:index>', methods=['GET'])
def get_one_merchant(index):
    print("the index", index)
    return jsonify(get_merchant_by_id(index))


app.run()
