#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import urljoin

from flask import Blueprint, jsonify, request, url_for

api = Blueprint('api', __name__)


# 有効なエンドポイントに誘導
@api.route('/')
def index():
    return jsonify(data=urljoin(request.host_url, url_for(('.materials'))))


@api.route('/materials')
@api.route('/materials/<id>')
def materials(id=None):
    from models import Material

    limit = request.args.get('limit', 20)

    materials = (Material.query.filter(Material.id == id) if id else Material.query) \
        .order_by(Material.updated_at.desc()).limit(limit)

    return jsonify(data=[material.serialize for material in materials])
