#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
@author: Zhige
@license: 
@contact: 303585825@qq.com
@software: pycharm
@file: restful.py
@time: 2019/12/8 0008 22:05
'''
from flask import jsonify
import json,decimal,datetime,time

# 定义服务器返回值，HTTPCode类，包含成功、授权错误、参数错误、服务器错误
# 所有函数都包含message、data两个参数，message用于传入错误信息，data用户传入返回数据
# message包含默认属性，可不传入，data默认为空，可不传入
# restful_result返回函数，将数据转为json格式

# success：成功
# unauth_error：授权错误
# params_error：参数错误
# server_error：服务器内部错误
# database_error：数据库错误


class HttpCode(object):
    ok = '200'
    unautherror = '401'
    paramserror = '400'
    servererror = '500'
    databaseerror = '402'

def restful_result(code,message,data):
    return jsonify({"code": code, "message": message, "data": data or {}})

def success(message="成功",data=None):
    return restful_result(code=HttpCode.ok,message=message,data=data)

def unauth_error(message="授权错误",data=None):
    return restful_result(code=HttpCode.unautherror,message=message,data=data)

def params_error(message="参数错误",data=None):
    return restful_result(code=HttpCode.paramserror,message=message,data=data)

def server_error(message="服务器内部错误",data=None):
    return restful_result(code=HttpCode.servererror,message=message,data=data)

def database_error(message="数据库错误",data=None):
    return restful_result(code=HttpCode.servererror,message=message,data=data)