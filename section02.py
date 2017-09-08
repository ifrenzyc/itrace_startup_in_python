# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Aa123456@127.0.0.1:3306/itrace_startup?charset=utf8"
db = SQLAlchemy(app)


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


class Cust(db.Model):
    cust_id = db.Column(db.Integer, primary_key=True, unique=True)
    area_id = db.Column(db.Integer)
    create_date = db.Column(db.Date)
    cust_group_id = db.Column(db.Integer)
    cust_name = db.Column(db.String(255))
    cust_number = db.Column(db.String(255))
    update_date = db.Column(db.Date)

    def __init__(self, cust_id, area_id, create_date, cust_group_id, cust_name, cust_number, update_date):
        self.cust_id = cust_id
        self.area_id = area_id
        self.create_date = create_date
        self.cust_group_id = cust_group_id
        self.cust_name = cust_name
        self.cust_number = cust_number
        self.update_date = update_date

    def __repr__(self):
        return '<Cust %r>' % self.cust_name


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
