# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2021/12/15 2:27
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from app import app
from .routes import Base_blue

app.register_blueprint(Base_blue)