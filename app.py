#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://nwpct1.hatenablog.com/entry/flask-libraries

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.init_app(app)

from controllers import api as api_v1_blueprint

app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
