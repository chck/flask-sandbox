#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://nwpct1.hatenablog.com/entry/flask-libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.init_app(app)


class Material(db.Model):
    __tablename__ = 't_materials'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.String(255), nullable=True, index=True)
    category = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=True, index=True)
    url = db.Column(db.String(255), unique=True, index=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, onupdate=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'category': self.category,
            'name': self.name,
            'url': self.url,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


@app.route('/')
def index():
    return 'Index Page'


@app.route('/materials')
@app.route('/materials/<id>')
def get_materials(id=None):
    limit = request.args.get('limit', 20)

    materials = (Material.query.filter(Material.id == id) if id else Material.query) \
        .order_by(Material.updated_at.desc()).limit(limit)

    return jsonify(data=[material.serialize for material in materials])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
