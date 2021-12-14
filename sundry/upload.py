# -*- encoding: utf-8 -*-
"""
@File    : upload.py
@Time    : 2021/12/15 2:33
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from flask_uploads import UploadSet, ALL
files = UploadSet('files', ALL)
