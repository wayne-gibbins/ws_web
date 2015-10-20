import requests
import os
import json

from flask import Flask, request, jsonify


app = Flask(__name__)
app.debug = True

def request_wants_json():
    best = request.accept_mimetypes \
            .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
            request.accept_mimetypes[best] > \
            request.accept_mimetypes['text/html']

def counter_tpl(counter):
    alot = ''
    if counter > 10 ** 9:
        alot = '<img src="http://cdn.thewritepractice.com/wp-content/uploads/2012/05/Alot-vs-a-lot1-600x450.png" />'

    return """<html>
<h1>page views</h1>
%s
<h2>%s</h2>
</html>""" % (alot, counter)

@app.route("/")
def index():
    count_resp = requests.get('http://api:5002/').text
    counter = int(json.loads(count_resp).get("counter", -1))
    #counter *= 5 * 10 ** 8
    if request_wants_json():
        return jsonify(counter=counter)
    return counter_tpl(counter)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
