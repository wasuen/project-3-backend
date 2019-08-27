import models

import os
import sys
import secrets


from flask import Blueprint, request, jsonify, url_for, send_file
from playhouse.shortcuts import model_to_dict

item = Blueprint('items', 'item', url_prefix='/item')

@item.route('/create', methods=["POST"])
def create():
    payload = request.form.to_dict()
    print(payload)
    item = models.Item.create(name=payload['name'],address=payload['address'])
    item_dict = model_to_dict(item)
    print(item_dict)
    return jsonify(data=item_dict, status={"code": 401, "message": "A user with that name or email exists"})