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
        print('hllo')
        # all_items = model_to_dict(models.Item.get(models.Item.user == 4))
        items = [model_to_dict(item) for item in models.Item.select()]
        print(items)
        return jsonify(data=items, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        print('doesnt work')
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})

@item.route('/create', methods=["POST"])
def create_item():
    # payload = request.form.to_dict()
    payload = request.get_json()
    print(payload)
    item = models.Item.create(**payload)
    item_dict = model_to_dict(item)
    return jsonify(data=item_dict, status={"code": 201, "message": "Success"})