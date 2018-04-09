from flask import Flask, jsonify, request

app = Flask(__name__)

inputs = [
  { 'name': 'randomString'}
]


@app.route('/inputs')
def get_inputs():
  return jsonify(inputs)


@app.route('/inputs', methods=['POST'])
def add_input():
  inputs.append(request.get_json())
  return '', 204
