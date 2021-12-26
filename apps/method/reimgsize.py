# -*- encoding: utf-8 -*-
"""
@File    : reimgsize.py
@Time    : 2021/12/19 1:22
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
import os
import math
import cv2
import time
import datetime

from apps import conf

# 获取原始大小（B）
def get_doc_size(path):
    try:
        size = os.path.getsize(path)
        return get_mb_size(size)
    except Exception as err:
        print(err)
# 获取原始大小（MB）
def get_mb_size(bytes):
    bytes = float(bytes)
    mb = bytes / 1024 / 1024
    return mb

# 删除文件
def delete_file(path):
    if file_exist(path):
        os.remove(path)
    else:
        print('no such file:%s' % path)
# 确认文件是否存在
def file_exist(path):
    return os.path.exists(path)

# 读取图片
def read_image(path):
    return cv2.imread(path)
# 保存图片
def save_image(path, image):
    cv2.imwrite(path, image)

# 压缩图片
def resize_rate(img, resize_path, fx, fy):
    im_resize = cv2.resize(img, None, fx=fx, fy=fy)
    save_image(resize_path, im_resize)

# 程序主题
def resize(info,before,img=None):
    size = get_doc_size(info.compress_path)
    resize_filename = before + '-' + info.num + '-' + str(time.time()).replace('.','') + '.jpg'
    resize_link = os.path.join(conf.reimgpath,datetime.datetime.today().strftime('%Y%m%d'))
    resize_path = os.path.join(conf.filepath,resize_link)

    # 是否有文件夹，如果没有则新建，有则忽略
    if not file_exist(resize_path):
        os.makedirs(resize_path)
    resize_link = os.path.join(resize_link,resize_filename)
    resize_path = os.path.join(resize_path,resize_filename)

    while size > conf.reimgsize:
        rate = math.ceil((size / conf.reimgsize) * 10) / 10 + 0.1
        rate = math.sqrt(rate)

        rate = 1.0 / rate

        if file_exist(resize_path):
            image = read_image(resize_path)
        else:
            if img is None:
                image = read_image(info.path)
            else:
                image = img

        resize_rate(image, resize_path, rate, rate)
        size = get_doc_size(resize_path)
    return resize_path,resize_link
