# -*- encoding: utf-8 -*-
"""
@File    : app_run.py
@Time    : 2021/12/15 2:16
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
import os
import sys

# # 基本配置
DEBUG = True
# FLASK_RUN_HOST = '0.0.0.0'
# FLASK_RUN_PORT = 80

# 配置数据库信息
from sundry.mysql import mysql_info

SQLALCHEMY_DATABASE_URI = mysql_info
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = -1

# uploads
UPLOADS_DEFAULT_DEST = 'uploads'

# 路径信息
BASE_PATH = os.path.dirname(os.path.realpath(sys.executable))
if not os.path.isdir(os.path.join(BASE_PATH, 'templates')):
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CONF_PATH = os.path.join(BASE_PATH, 'conf', 'conf.json')

PROJECT_NAME = 'OURAN_FUZHUANGDD'
