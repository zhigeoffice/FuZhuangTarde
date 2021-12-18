# -*- encoding: utf-8 -*-
"""
@File    : save.py
@Time    : 2021/12/16 23:48
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
import os
import time
from threading import Thread

import cv2

from apps import conf
from exts import db
from models.img import ImgSheji
from sundry.upload import files
from utiles import restful

def set_wh(model, img_id):
    img_info = db.session.query(model).filter(model.num == img_id).first()
    img = cv2.imread(img_info.path)
    try:
        img_info.width = img.shape[0]  # 宽
        img_info.height = img.shape[1]  # 高
        db.session.commit()
    except:
        pass

def start_set_wh(model, img_id):
    t = Thread(target=set_wh, args=(model, img_id))
    t.run()

def save_shejitu(file):
    filename = file.filename
    img_id = os.path.splitext(filename)[0]
    file_format = os.path.splitext(filename)[1]
    if len(img_id) > 29:
        img_id = 'o_' + str(int(time.time() * (10 ** 6)))
    else:
        sql_shejitu = db.session.query(ImgSheji).filter(ImgSheji.num == img_id).all()
        if len(sql_shejitu):
            img_id = 'o_' + str(int(time.time() * (10 ** 6)))

    filename = img_id + file_format

    sheji = ImgSheji(
        filename=filename,  # 文件名
        path=os.path.join(conf.filepath,conf.path_shejitu, filename),  # 文件路径
        link=os.path.join(conf.path_shejitu, filename),  # 文件路径
        num=img_id #编号
    )
    db.session.add(sheji)
    db.session.commit()

    files.save(file, os.path.join(conf.filepath,conf.path_shejitu), filename)

    start_set_wh(ImgSheji, img_id)

    data = {'message': img_id, 'filename': img_id + file_format}
    return restful.success(data=data)
