from app import app
from db import db

__author__ = 'khalilj'
__creation_date__ = '08/29/2018'

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
