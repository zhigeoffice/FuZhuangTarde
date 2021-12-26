# -*- encoding: utf-8 -*-
"""
@File    : common.py
@Time    : 2021/12/25 22:55
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from . import Base_blue as blue
from utiles import restful
from flask import request
from exts import db
from models import parameter
from utiles.model_to_dict import queryToDict as todict


@blue.route('/common/get/system-info', methods=['POST'])
def getSystemInfo():
    drive = {
        'driveSize': 500000,
        'usedSize': 300000,
        'usedPercent': 30,
        'cacheSize': 600
    }
    data = {
        'drive': drive
    }
    return restful.success(data=data)


parameters = {
    'Size':parameter.Size,
    'Color':parameter.Color,
    'Buliao':parameter.Buliao,
    'Fengge':parameter.Fengge,
    'Leixing':parameter.Leixing
}
@blue.route('/common/get/parameter',methods=['POST'])
def getParameter():
    req = request.get_json()
    model = parameters[req['cls']]
    try:
        sql = db.session.query(model).filter(model.state != -1).all()
        return restful.success(data=todict(sql))
    except:
        return restful.database_error(message='数据库连接错误，请重试，多次失败请联系管理员')

@blue.route('/common/set/parameter',methods=['POST'])
def setParameter():
    req = request.get_json()
    print(req)
    return restful.success()

@blue.route('/common/create/parameter',methods=['POST'])
def createParameter():
    req = request.get_json()
    model = parameters[req['cls']]
    try:
        sql = db.session.query(model).filter(model.name == req['text']).all()
        if len(sql):
            return restful.database_error(message='这个类名数据库中已经有了')
        db.session.add(model(name=req['text']))
        db.session.commit()
        return restful.success()
    except:
        return restful.database_error(message='数据库连接错误，请重试，多次失败请联系管理员')