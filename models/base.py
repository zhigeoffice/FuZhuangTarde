#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : zhige
@contact : 303585825@qq.com
@Software: PyCharm
@project : ouran_fuzhuangxitong
@File    : base
@Time    : 2021/9/2
'''
from exts import db
import datetime

# 订单列表
class Order(db.Model):
    _tablename_ = 'order'

    id = db.Column(db.String(50),primary_key=True) # id
    number = db.Column(db.String(100)) # 订单编号
    member = db.Column(db.String(100)) # 客户姓名
    phone = db.Column(db.String(100)) # 联系方式
    shopname = db.Column(db.String(100)) # 店铺名称
    dealnum = db.Column(db.String(100)) # 交易编号
    staff_id =  db.Column(db.Integer) # 绑定员工
    address = db.Column(db.String(100)) # 地址
    join_time = db.Column(db.DateTime,default=datetime.datetime.now)


# 产品列表
class Cargo(db.Model):
    _tablename_ = 'cargo'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True) # id
    order_id = db.Column(db.String(50)) # 订单编号
    xuhao = db.Column(db.Integer) # 订单编号
    guige = db.Column(db.String(100)) # 规格
    size = db.Column(db.String(10)) # 大小
    count = db.Column(db.Integer) # 数量
    shejitu = db.Column(db.String(100)) # 设计图名称
    beizhu = db.Column(db.String(100))
    shengchantu = db.Column(db.String(100)) # 生产图名称
    join_time = db.Column(db.DateTime,default=datetime.datetime.now)

# 员工列表
class Staff(db.Model):
    _tablename_ = 'staff'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True) # id
    # name = db.Column(db.String(20)) # 姓名
    # state = db.Column(db.Integer) # 状态
    join_time = db.Column(db.DateTime,default=datetime.datetime.now)

class Img(db.Model):
    _tablename_ = 'img'

    id = db.Column(db.String(255),primary_key=True) # id
    filename = db.Column(db.String(50))
    path = db.Column(db.String(255))