# -*- coding:utf-8 -*-

'''
数据库例子
'''

from . import db


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
