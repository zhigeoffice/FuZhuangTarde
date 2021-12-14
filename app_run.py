# -*- encoding: utf-8 -*-
"""
@File    : app_run.py
@Time    : 2021/12/15 2:16
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from apps import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
