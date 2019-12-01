from flask import Flask
from flask import render_template
from flask import jsonify

import socket

app = Flask(__name__)

@app.route("/")
def hello():
    response = {"value": "Hello from Kubernetes!", "ip": getIp(getHost()), "host": getHost()}
    print ("Responding {} ...".format(response))
    return jsonify(response)

@app.route('/store')
def index():
  return render_template('index.html')

def getIp(hostname):
    return socket.gethostbyname(hostname)

def getHost():
    return socket.gethostname()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
