# -*- encoding: utf-8 -*-
"""
@File    : getimg.py
@Time    : 2021/12/17 16:23
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""

from exts import db
from models.img import ImgSheji
from utiles import restful
from utiles.model_to_dict import queryToDict as to_dict

def getshejitulist(req):
    # 获取请求变量
    pages = req['pagesize']
    page = req['page']
    sort = req['sort']
    # 设置查询条件
    sql = db.session.query(ImgSheji)
    sort = ImgSheji.addtime.desc() if sort else ImgSheji.addtime.asc()
    ## 获取数据数量
    count = sql.count()
    ## 设置查询区间
    start = (page-1) * pages
    end = start + pages
    print(page,'-',pages)
    print(start,'-',end)
    sql = sql.order_by(sort).slice(start,end)
    #开始查询并返回数据
    imgs = sql.all()
    data = {
        'imgs':to_dict(imgs),
        'count':count
    }
    return restful.success(data=data)