#!/usr/bin/env python

from __future__ import print_function
from flask_restful import Resource, reqparse
from models.user import UserModel

__author__ = 'khalilj'
__creation_date__ = '08/26/2018'


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This filed cannot be blank"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This filed cannot be blank"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
