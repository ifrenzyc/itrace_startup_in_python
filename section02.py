# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/itsyc/openstack")
def openstack():
    action = request.args.get('action')
    return {
        "create": "running",
        "suspend": "suspended",
        "pause": "paused",
        "unpause": "running",
        "resume": "running",
        "stop": "stoped"
    }.get(action, "error")
