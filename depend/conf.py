# -*- encoding: utf-8 -*-
"""
@File    : conf.py
@Time    : 2021/12/17 0:02
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from config import CONF_PATH
import json


class Conf(object):
    def __init__(self):
        self.info = {}
        self.read_conf()

    def read_conf(self):
        print('---read config----')
        with open(CONF_PATH, 'r') as f:
            self.info = json.load(f)

    def update_conf(self):
        with open(CONF_PATH, 'w') as f:
            json.dump(self.info, f)

    @property
    def filepath(self):
        return self.info['filepath']

    @property
    def path_shejitu(self):
        return self.info['imgpath']['shejitu']

    @property
    def path_chanpinpeijian(self):
        return self.info['imgpath']['chanpinpeijian']

    @property
    def path_shengchantu(self):
        return self.info['imgpath']['shengchantu']

    @property
    def path_sucaitu(self):
        return self.info['imgpath']['sucaitu']

    @property
    def path_yulantu(self):
        return self.info['imgpath']['yulantu']

    @property
    def path_other(self):
        return self.info['imgpath']['other']

    @property
    def reimgsize(self):
        return self.info['reimgsize']

    @property
    def reimgpath(self):
        return self.info['reimgpath']


conf = Conf()
