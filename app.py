import requests
import os

from flask import Flask, jsonify


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    msg = requests.get('http://mattapi:5002/').text
    return jsonify(msg=msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
