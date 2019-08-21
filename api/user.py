# this is like the controller in express

import models
# obviously the models, models.Dog, models.User

import os
import sys
import secrets
### ignoring at the moment

from flask import Blueprint, request, jsonify, url_for, send_file
# Blueprint - they record opertions to execute,
# thier controllers
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict # from peewee

# first argument, is the blueprint name
# second arg - is its import name
# 3 arg = this is what every route in the blueprint
# should start with much app.use('/api/v1', fruitsController)

# this will have to be registered in the app.py file
user = Blueprint('users', 'user', url_prefix='/user')


# def save_picture(form_picture):
#     # this function has to do with the module Pillow
#     # PIL
#     # purpose is to save the image as a static asset
#     # 1. generate a random name
#     random_hex = secrets.token_hex(8)# generates a random integer

#     # grabbing the ext , jpeg, jpg
#     f_name, f_ext = os.path.splitext(form_picture.filename)
#     # => ['jimProfile', 'png']
#     # create the random picture name with the correct extension
#     picture_name = random_hex + f_ext

#     # create the file_path
#     file_path_for_avatar = os.path.join(os.getcwd(), 'static/profile_pics/' + picture_name)

#     # Pillow code stars
#     output_size = (125, 175) # set the size of picture, as tuple
#     # open the file sent from the client
#     i = Image.open(form_picture)
#     i.thumbnail(output_size) # set the size accepts a tuple with dimensions
#     i.save(file_path_for_avatar) # save it to file path we created

#     return picture_name

@user.route('/register', methods=["POST"])
def register():
    print(request)
    print(type(request))
    # this is how we grab the image being sent over
    pay_file = request.files
    # this has the form info in teh dict
    # we change the request object into a dictionary so
    # we can see inside it
    payload = request.form.to_dict()
    dict_file = pay_file.to_dict()


    print(payload)
    print(dict_file)

    payload['email'].lower() # make emails all lower case!
    try:
        # check to see if the email exist, if it does let the user know
        models.User.get(models.User.email == payload['email'])# query
        # trying to find a user by thier email
        #if models.User.get exists then respond to the client
        return jsonify(data={}, status={"code": 401, "message": "A user with that name or email exists"})
    except models.DoesNotExist: # boolean on the model
        # otherwise create and register the user

        # hash password using bcrypt
        payload['password'] = generate_password_hash(payload['password'])
        # function that will save the image as a static asset in our static
        # file_picture_path = save_picture(dict_file['file'])
        # # save_picture is helper function we will create

        # add the image property to payload dictionary and
        #  save the file_path of our image in the db
        # payload['image'] = file_picture_path

        ## Create the ROw in the sql table
        user = models.User.create(**payload) # the spread operator in javascript
        # same as above this is the longhand
        print(type(user)) #> class User user is an instance of class
        # user = models.User.create(username=payload['username'], password=payload['password'])
        # start the user session
        login_user(user) # login_user is from flask_login, will set user id in session

        # current_user.image = file_picture_path # and the picture so we have it whenever

        # we can't send back a class we can only send back dicts, lists
        user_dict = model_to_dict(user)
        # make our response object jsonifyable
        # lists, hashs, simple datatype like number bools,
        # NO class or instance of class
        print(user_dict)
        print(type(user_dict))

        # remove the password, client doesn't need to know
        del user_dict['password']

        return jsonify(data=user_dict, status={"code": 201, "message": "Success"})