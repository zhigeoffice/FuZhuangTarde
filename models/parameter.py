# -*- encoding: utf-8 -*-
"""
@File    : parameter.py
@Time    : 2021/12/26 4:23
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from exts import db
import datetime

class Buliao(db.Model):
    _tablename_ = 'buliao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    name = db.Column(db.String(20))  # 材料名称
    state = db.Column(db.Integer,default=1)  # 状态 -1 删除 0 不可用 1可用
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

class Fengge(db.Model):
    _tablename_ = 'fengge'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    name = db.Column(db.String(20))  # 材料名称
    state = db.Column(db.Integer,default=1)  # 状态 -1 删除 0 不可用 1可用
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

class Color(db.Model):
    _tablename_ = 'color'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    name = db.Column(db.String(20))  # 材料名称
    state = db.Column(db.Integer,default=1)  # 状态 -1 删除 0 不可用 1可用
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

class Size(db.Model):
    _tablename_ = 'size'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    name = db.Column(db.String(20))  # 材料名称
    state = db.Column(db.Integer,default=1)  # 状态 -1 删除 0 不可用 1可用
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

class Leixing(db.Model):
    _tablename_ = 'leixing'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    name = db.Column(db.String(20))  # 材料名称
    state = db.Column(db.Integer,default=1)  # 状态 -1 删除 0 不可用 1可用
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)