#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
@author: Zhige
@license: 
@contact: 303585825@qq.com
@software: pycharm
@file: model_to_dict.py
@time: 2019/12/14 0014 23:03
'''
# 将sqlalchemy中model返回对象转换为字典格式，
# models为传入的model对象
# change为是否改变值得格式【0：不转换，1：转换】

from datetime import datetime as cdatetime  # 有时候会返回datatime类型
from datetime import date, time
from decimal import Decimal
from flask_sqlalchemy import Model
from sqlalchemy import DateTime, Numeric, Date, Time  # 有时又是DateTime


def queryToDict(models,change=1):
    if not(len(models)):
        return []
    if not (change==0 or change==1):
        raise ValueError('change只能为1或0')
    try:
        if (isinstance(models, list)):
            if (isinstance(models[0], Model) or isinstance(models, Model)):
                lst = []
                for model in models:
                    gen = model_to_dict(model,change)
                    dit = dict((g[0], g[1]) for g in gen)
                    lst.append(dit)
                return lst
            else:
                res = result_to_dict(models,change)
                return res
        else:
            if (isinstance(models, Model)):
                gen = model_to_dict(models,change)
                dit = dict((g[0], g[1]) for g in gen)
                return dit
            else:
                res = dict(zip(models.keys(), models))
                if change:
                    find_datachange(res)
                return res
    except:
        gen = model_to_dict(models,change)
        dit = dict((g[0], g[1]) for g in gen)
        return dit


# 当结果为result对象列表时，result有key()方法
def result_to_dict(results,change):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    if change:
        for r in res:
            find_datachange(r)
    return res


def model_to_dict(model,change):  # 这段来自于参考资源
    for col in model.__table__.columns:
        if change:
            if isinstance(col.type, (DateTime,cdatetime,date,time,Time,Date)):
                value = convert_datetime(getattr(model, col.name))
            elif isinstance(col.type, (Numeric,Decimal)):
                value = str(getattr(model, col.name))
            else:
                value = getattr(model, col.name)
        else:
            value = getattr(model, col.name)

        yield (col.name, value)


def find_datachange(value):
    for v in value:
        if (isinstance(value[v], (cdatetime,date,time))):
            value[v] = convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改
        elif isinstance(value[v],(Numeric,Decimal)):
            value[v] = str(value[v])


def convert_datetime(value):
    if value:
        if (isinstance(value, (cdatetime, DateTime))):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif (isinstance(value, (date, Date))):
            return value.strftime("%Y-%m-%d")
        elif (isinstance(value, (Time, time))):
            return value.strftime("%H:%M:%S")
    else:
        return ""
