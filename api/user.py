import models

import os
import sys
import secrets


from flask import Blueprint, request, jsonify, url_for, send_file
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user', url_prefix='/user')

@user.route('/register', methods=["POST"])
def register():
    print(request)
    print(type(request))
    payload = request.form.to_dict()
    print(payload)

    payload['email'].lower()
    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(data={}, status={"code": 401, "message": "A user with that name or email exists"})

    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        user = models.User.create(**payload)
        print(type(user))
        login_user(user)
        user_dict = model_to_dict(user)
        print(user_dict)
        print(type(user_dict))

        del user_dict['password']

        return jsonify(data=user_dict, status={"code": 201, "message": "Success"})

@user.route('/login', methods=["POST"])
def login():
    payload = request.get_json()
    print(payload, '< --- this is playload')
    try:
        user = models.User.get(models.User.email== payload['email'])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            print(user, ' this is user')
            return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
        else:
            return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})
        
@user.route('/logout')
def logout():
  logout_user()
  return jsonify(status={"code": 200, "message": "logged out"})

@user.route('<id>/items', methods=["GET"])
def get_user_items(id):

    user = models.User.get_by_id(id)
    print(user.items, '.users')


    items = [model_to_dict(item) for item in user.items]

    def delete_key(item, key):
        del item[key]
        return item

    item_without_user = [delete_key(item, 'user') for item in items]

    return jsonify(data=dog_without_user, status={"code": 200, "message": "Success"})

