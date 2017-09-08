# -*- coding:utf-8 -*-

from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Aa123456@127.0.0.1:3306/itrace_startup?charset=utf8"
