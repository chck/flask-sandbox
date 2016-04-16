#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db


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
