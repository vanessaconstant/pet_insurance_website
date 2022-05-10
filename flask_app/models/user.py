
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

import re
from flask import session, flash, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.pets = []

    @classmethod
    def createUser(cls, data):

        if not cls.validateReg(data):
            return False

        data = cls.parsed_data(data)

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        user_id = result
        session['user_id'] = user_id

        return user_id

    @classmethod
    def get_user_by_id(cls, id):

        data = {
            'id': id
        }

        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        if result:
            result = cls(result[0])
        return result

    @classmethod
    def get_user_by_email(cls, email):

        data = {
            'email': email
        }

        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        if result:
            result = cls(result[0])
        return result

    @classmethod
    def loginUser(cls, data):
        if not User.get_user_by_email(data['email']):
            flash("You have entered a wrong email or password. Please try again", "login")
            return False

        user_info = User.get_user_by_email(data['email'])
        if not bcrypt.check_password_hash(user_info.password, data['password']):
            flash('You have entered a wrong email or password', "login")
            return False
        session["user_id"] = user_info.id

        return user_info

    @staticmethod
    def validateReg(data):
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True

        if not EMAIL_REGEX.match(data['email']):
            flash("This is not a valid email! Please try again.", "register")
            is_valid = False
        if User.get_user_by_email(data['email']):
            flash("Already have an account. Please login.", "register")
            is_valid = False
        if(len(data['first_name']) < 3):
            flash("First name requires at least 3 characters.", "register")
            is_valid = False
        if(len(data['last_name']) < 3):
            flash("Last name requires at least 3 characters.", "register")
            is_valid = False
        if(len(data['password']) < 8):
            flash("Password requires at least 8 characters.", "register")
            is_valid = False
        if(data['password'] != data['conf_password']):
            flash("Password does not match.", "register")
            is_valid = False

        return is_valid

    @staticmethod
    def parsed_data(data):

        data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': bcrypt.generate_password_hash(data['password'])

        }

        return data
