from peewee import *
from flask_login import UserMixin 
import datetime 

DATABASE = SqliteDatabase('users.sqlite')

class User(UserMixin, Model):
    username = CharField() 
    email = CharField()
    password = CharField()

    class Meta:
        # when the class object creates an object
        # we can give it instructions
        database = DATABASE


# class (Model):
#     name = CharField()
#     owner = CharField()
#     breed = CharField()
#     user = ForeignKeyField(User, backref='dogs')
#     created_at = DateTimeField(default=datetime.datetime.now)

#     class Meta:
#         database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    print("TABLES CREATED")
    DATABASE.close()



