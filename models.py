from peewee import *
from flask_login import UserMixin 
import datetime

import os

from playhouse.db_url import connect

DATABASE = connect(os.environ.get('DATABASE_URL'))

DATABASE = SqliteDatabase('users.sqlite')

class User(UserMixin, Model):
    username = CharField() 
    email = CharField()
    password = CharField()

    class Meta:
        database = DATABASE


class items(Model):
    name = CharField()
    submittedBy = CharField()
    user = ForeignKeyField(User, backref='dogs')
    created_at = DateTimeField(default=datetime.datetime.now)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    print("TABLES CREATED")
    DATABASE.close()

