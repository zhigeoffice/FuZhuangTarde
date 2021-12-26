# -*- encoding: utf-8 -*-
"""
@File    : app_run.py
@Time    : 2021/12/15 2:16
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from models import base, guize, img, parameter

CMSUser = base.BaseMember
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username='李风阅', password='123123', email='lifengyue@xiaoranwenhua.com'):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('员工添加成功！')


if __name__ == '__main__':
    manager.run()
