from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

from flask import session, flash, session


class Pet:

    def __init__(self, data):
        self.id = data['id']
        self.pet_name = data['pet_name']
        self.birthday = data['birthday']
        self.breed = data['breed']
        self.user_id = data['user_id']
        self.claims = []

    @classmethod
    def createPet(cls, data):

        query = "INSERT INTO pets (pet_name, birthday, breed, user_id, created_at, updated_at) VALUES(%(pet_name)s, %(birthday)s, %(breed)s, %(user_id)s, NOW(), NOW());"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        pet_id = result

        return pet_id

    @classmethod
    def get_pet_by_id(cls, id):

        data = {
            'id': id
        }

        query = "SELECT * FROM pets WHERE id = %(id)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        if result:
            result = cls(result[0])
        return result

    @classmethod
    def get_all_pets(cls, id):

        pets = []

        data = {
            'id': id
        }

        query = "SELECT * FROM pets  WHERE user_id = %(id)s;"
        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        if result:
            for pet in result:

                pets.append(cls(pet))

        return pets
