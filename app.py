# -*- encoding: utf-8 -*-
"""
@File    : app_run.py
@Time    : 2021/12/15 2:16
@Author  : zhige
@Email   : zhigeoffice@gmail.com
@Software: PyCharm
"""
from flask import Flask
import config
from exts import db
from sundry.upload import files
from flask_uploads import configure_uploads
import os
from flask_migrate import Migrate

migrate = Migrate()

def caeate_app():
    fun_app = Flask(__name__,
                    template_folder=os.path.join(config.BASE_PATH, 'templates'),
                    static_folder=os.path.join(config.BASE_PATH, 'static'))

    fun_app.config.from_object(config)
    configure_uploads(fun_app, files)
    db.init_app(fun_app)
    migrate.init_app(fun_app, db)
    return fun_app


app = caeate_app()
