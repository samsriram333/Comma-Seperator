from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)
@app.route('/integer', methods = ['POST'])
def integer():
    data = request.get_json()
    filename = data['FilePath']
    numbers = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            number = int(line.strip())
            numbers.append(number)
    output = ','.join('{}'.format(s) for s in numbers)
    return output


# def integer():
#     data = request.get_json()
#     filename = data.get('FilePath')
#     if not filename:
#         return jsonify({"error": "FilePath is missing in the request"}), 400
#     try:
#         with open(filename) as f:
#             lines = f.readlines()
#             numbers = [int(line.strip()) for line in lines if line.strip().isnumeric()]
#     except FileNotFoundError:
#         return jsonify({"error": "File not found"}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     output = ','.join('{}'.format(s) for s in numbers)
#     return jsonify({"output": output})

@app.route('/strings', methods = ['POST'])
def strings():
    data = request.get_json()
    filename = data['FilePath']
    numbers = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            number = str(line.strip())
            numbers.append(number)
    output = ','.join('"{}"'.format(s) for s in numbers)
    return output

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)