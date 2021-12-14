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
from models import base

def caeate_app():
    app = Flask(__name__,
                template_folder=os.path.join(config.BASE_PATH,'templates'),
                static_folder=os.path.join(config.BASE_PATH,'static'))

    app.config.from_object(config)
    configure_uploads(app, files)
    db.init_app(app)
    migrate.init_app(app, db)
    return app

app = caeate_app()
