# -*- encoding: utf-8 -*-
"""
@File    : upload.py
@Time    : 2021/12/16 21:43
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from . import Base_blue
from flask import request, jsonify, render_template
from sundry.upload import files
from config import BASE_PATH
from apps.method.save import save_shejitu
from apps.method.getimg import getshejitulist


@Base_blue.route('/upload/shejitu', methods=['POST'])
def upload_shejitu():
    m = request.files['file']
    if m.filename == '':
        return jsonify({'result': False, 'message': '文件不能为空'})
    return save_shejitu(m)

@Base_blue.route('/get/img/shejitu-list', methods=['POST'])
def getimglist():
    req = request.get_json()
    return getshejitulist(req)
