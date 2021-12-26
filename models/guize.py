# -*- encoding: utf-8 -*-
"""
@File    : guize.py
@Time    : 2021/12/15 17:58
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from exts import db
import datetime


class GuizeShengchanPaiban(db.Model):
    """
    生产图排版规则
    """
    _tablename_ = 'guize_shengchan_paiban'

    id = db.Column(db.String(255), primary_key=True)  # id
    filename = db.Column(db.String(50))  # 文件名
    path = db.Column(db.String(255))  # 文件路径
    width = db.Column(db.Integer)  # 宽
    height = db.Column(db.Integer)  # 高
    num = db.Column(db.String(30))  # 编码
    member_id = db.Column(db.Integer)  # 设计员工ID
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 加入时间
    size = db.Column(db.String(30))  # 尺寸
    materials = db.Column(db.String(30))  # 材料
    label = db.Column(db.String(255))  # 标签
    note = db.Column(db.String(255)) # 备注
