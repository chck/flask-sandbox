#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://nwpct1.hatenablog.com/entry/flask-libraries
from urllib.parse import urljoin

from flask import Flask, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.init_app(app)


# 有効なエンドポイントに誘導
@app.route('/')
def index():
    return jsonify(data=urljoin(request.host_url, url_for(('.materials'))))


@app.route('/materials')
@app.route('/materials/<id>')
def materials(id=None):
    from models import Material

    limit = request.args.get('limit', 20)

    materials = (Material.query.filter(Material.id == id) if id else Material.query) \
        .order_by(Material.updated_at.desc()).limit(limit)

    return jsonify(data=[material.serialize for material in materials])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
