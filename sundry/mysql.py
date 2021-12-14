# -*- encoding: utf-8 -*-
"""
@File    : mysql.py
@Time    : 2021/12/15 2:36
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
mysql = dict(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'gezi',
    db = 'fuzhuangdingdan',
    charset = 'utf8mb4'
    )
mysql_info = 'mysql+pymysql://%s:%s@%s:%d/%s?charset=%s'%(mysql['user'],
                                                      mysql['password'],
                                                      mysql['host'],
                                                      mysql['port'],
                                                      mysql['db'],
                                                      mysql['charset'])