# -*- coding:utf-8 -*-


from flask import request
from db.cust import Cust

from . import app


@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


current_stat = ""


@app.route("/<username>", methods=['GET'])
def hello_with_username(username):
    return "Hello " + username + "!"


@app.route("/itsyc/openstack", methods=['GET'])
def openstack():
    global current_stat

    action = request.args.get('action')
    step = current_stat + "|" + action

    if "|create" == step:
        current_stat = "running"
    elif "running|suspend" == step:
        current_stat = "suspended"
    elif "running|pause" == step:
        current_stat = "paused"
    elif "suspended|resume" == step:
        current_stat = "running"
    elif "paused|unpause" == step:
        current_stat = "running"
    elif "running|stop" == step:
        current_stat = "stop"
    else:
        return "error"
    return current_stat


@app.route("/cust/get")
def get_cust():
    cust = Cust.query.all()
    return cust[0].cust_name


def run_app():
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
