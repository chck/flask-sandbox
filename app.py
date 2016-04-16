#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/materials/')
@app.route('/materials/<id>')
def show_materials(id=None):
    return 'xxx %s' % id


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
