# -*- encoding: utf-8 -*-
"""
@File    : img.py
@Time    : 2021/12/15 17:34
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from exts import db
import datetime


class ImgYuanshi(db.Model):
    """
    原始图
    """
    _tablename_ = 'img_yuanshi'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    filename = db.Column(db.String(50))  # 文件名
    path = db.Column(db.String(255))  # 文件路径
    link = db.Column(db.String(255))  # 引用连接
    width = db.Column(db.Integer)  # 宽
    height = db.Column(db.Integer)  # 高
    num = db.Column(db.String(255))  # 编码
    creation_data = db.Column(db.DateTime, default=datetime.datetime.now)  # 加入时间
    compress = db.column(db.String(100)) # 压缩图位置
    note = db.Column(db.String(255)) # 备注


class ImgSheji(db.Model):
    """设计图"""
    _tablename_ = 'img_sheji'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    filename = db.Column(db.String(255))  # 文件名
    path = db.Column(db.String(255))  # 文件路径
    link = db.Column(db.String(255))  # 引用连接
    width = db.Column(db.Integer)  # 宽
    height = db.Column(db.Integer)  # 高
    num = db.Column(db.String(30))  # 编码
    member_id = db.Column(db.Integer)  # 设计员工ID
    creation_data = db.Column(db.DateTime, default=datetime.datetime.now)  # 加入时间
    compress = db.column(db.String(100)) # 压缩图位置
    note = db.Column(db.String(255)) # 备注


class ImgShengchan(db.Model):
    """
    生产图
    """
    _tablename_ = 'img_shengchan'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    filename = db.Column(db.String(50))  # 文件名
    path = db.Column(db.String(255))  # 文件路径
    link = db.Column(db.String(255))  # 引用连接
    width = db.Column(db.Integer)  # 宽
    height = db.Column(db.Integer)  # 高
    num = db.Column(db.String(30))  # 编码
    member_id = db.Column(db.Integer)  # 设计员工ID
    creation_data = db.Column(db.DateTime, default=datetime.datetime.now)  # 加入时间
    size = db.Column(db.String(30))  # 尺寸
    materials = db.Column(db.String(30))  # 材料
    label = db.Column(db.String(255))  # 标签
    compress = db.column(db.String(100)) # 压缩图位置
    note = db.Column(db.String(255)) # 备注


class ImgXiaoguo(db.Model):
    """
    效果图
    """
    _tablename_ = 'img_xiaoguo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    filename = db.Column(db.String(50))  # 文件名
    path = db.Column(db.String(255))  # 文件路径
    link = db.Column(db.String(255))  # 引用连接
    width = db.Column(db.Integer)  # 宽
    height = db.Column(db.Integer)  # 高
    num = db.Column(db.String(30))  # 编码
    member_id = db.Column(db.Integer)  # 设计员工ID
    creation_data = db.Column(db.DateTime, default=datetime.datetime.now)  # 加入时间
    size = db.Column(db.String(30))  # 尺寸
    materials = db.Column(db.String(30))  # 材料
    label = db.Column(db.String(255))  # 标签
    compress = db.column(db.String(100)) # 压缩图位置
    note = db.Column(db.String(255)) # 备注


class ImgYuanshiShengchan(db.Model):
    """
    原始生产图
    """
    _tablename_ = 'img_yuanshi_shengchan'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id
    chanpin_id = db.Column(db.String(50))  # 产品名称
    weizhi = db.Column(db.String(255))  # 所属位置
    path = db.Column(db.String(255))  # 文件路径
    link = db.Column(db.String(255))  # 引用连接
    width = db.Column(db.Integer)  # 宽
    height = db.Column(db.Integer)  # 高
    num = db.Column(db.String(30))  # 编码
    member_id = db.Column(db.Integer)  # 设计员工ID
    creation_data = db.Column(db.DateTime, default=datetime.datetime.now)  # 加入时间
    size = db.Column(db.String(30))  # 尺寸
    materials = db.Column(db.String(30))  # 材料
    label = db.Column(db.String(255))  # 标签
    compress = db.column(db.String(100)) # 压缩图位置
    note = db.Column(db.String(255)) # 备注
