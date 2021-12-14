# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2021/12/15 2:28
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from . import Base_blue
from models import base

@Base_blue.route('/',methods=['GET'])
def main():
    return '123'