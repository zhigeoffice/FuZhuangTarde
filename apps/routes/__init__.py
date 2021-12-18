# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2021/12/15 4:50
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from flask import Blueprint

Base_blue = Blueprint('Base',__name__)

from . import main
from . import shejitu