import models

import os
import sys
import secrets


from flask import Blueprint, request, jsonify, url_for, send_file
from playhouse.shortcuts import model_to_dict

item = Blueprint('items', 'item', url_prefix='/item')

@item.route('/create', methods=["POST"])
def register():
    print(request)
    print(type(request))
    pay_file = request.files
    payload = request.form.to_dict()
    dict_file = pay_file.to_dict()
    print(payload)
    print(dict_file)

    payload['email'].lower()
    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(data={}, status={"code": 401, "message": "A user with that name or email exists"})