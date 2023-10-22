from dataStore import BaseDB
from flask import Flask, jsonify, request
import json


app = Flask(__name__)


database = BaseDB()


@app.route("/get/<key>", methods=["GET"])
def get(key):
    value = database.get(key)
    if value:
        return jsonify({"value": value})
    else:
        return "Key not found", 404


@app.route("/getall", methods=["GET"])
def getall():
    values = database.keys()
    return jsonify(values)


@app.route("/set", methods=["POST"])
def set():
    key = request.args.get("key")
    value = request.args.get("value")
    if key and value:
        database.set(key, value)
        return "OK"
    else:
        return "Invalid data", 400


@app.route("/delete<key>", methods=["DELETE"])
def delete(key):
    if database.exists(key):
        database.delete(key)
        return "Key deleted"
    else:
        return "key not found", 404


if __name__ == "__main__":
    app.run(debug=True)
