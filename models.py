from peewee import *
from flask_login import UserMixin 
import datetime

import os

from playhouse.db_url import connect

# DATABASE = connect(os.environ.get('DATABASE_URL'))

DATABASE = SqliteDatabase('usersss.sqlite')

class User(UserMixin, Model):
    username = CharField() 
    email = CharField()
    password = CharField()
    class Meta:
        database = DATABASE

class Item(Model):
    name = CharField()
    address = CharField()
    user_id = ForeignKeyField(User, backref='item')
    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Item], safe=True)
    print("TABLES CREATED")
    DATABASE.close()

