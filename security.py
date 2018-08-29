#!/usr/bin/env python

from __future__ import print_function
from models.user import UserModel
from werkzeug.security import safe_str_cmp

__author__ = 'khalilj'
__creation_date__ = '08/26/2018'


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


