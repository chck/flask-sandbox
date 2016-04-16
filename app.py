#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/materials/')
@app.route('/materials/<id>')
def get_materials(id=None):
    limit = request.args.get('limit', 20)
    return jsonify(id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
