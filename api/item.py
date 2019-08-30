import models

import os
import sys
import secrets


from flask import Blueprint, request, jsonify, url_for, send_file
from playhouse.shortcuts import model_to_dict

item = Blueprint('items', 'item', url_prefix='/item')

@item.route('/showitems', methods=["GET"])
def get_all_items():
    try:
        items = [model_to_dict(item) for item in models.Item.select()]
        return jsonify(data=items, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})

@item.route('/create', methods=["POST"])
def create_item():
    payload = request.form.to_dict()
    item = models.Item.create(**payload)
    item_dict = model_to_dict(item)
    return jsonify(data=item_dict, status={"code": 201, "message": "Success"})

# @item.route('/<id>', methods=["GET"])
# def get_user_items(id):
#     items = models.User.get(models.Item.user == payload['id']
#     return jsonify(data=items, status={"code": 200, "message": "Success"})

# @home.route('/<id>/edit', methods=["PUT"])
# def update_home(id):
#   pay_file = request.files
#   print(pay_file)
#   payload = request.form.to_dict()
#   dict_file = pay_file.to_dict()
#   print(dict_file)
#   file_picture_path = save_picture(dict_file['file'])
#   payload['image'] = file_picture_path
#   query =  models.Home.update(**payload).where(models.Home.id == id)
#   query.execute() # run the query, must do for update and delete
#   # excuse as per docs returns the row updated

#   # if we want to return the update resource we have to find it
#   updated_home = models.Home.get_by_id(id)


#   return jsonify(data=model_to_dict(updated_home), status={"code": 200, "message": "Success"})

 
# @home.route('/<id>/delete', methods=["DELETE"])
# def delete_home(id):
#   query = models.Home.delete().where(models.Home.id == id)
#   query.execute()

#   return jsonify(data="resource successfully deleted", status={"code": 200, "message": "Home deleted"})
