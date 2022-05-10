from unittest import result
from flask_app import app
from flask_app.models import pet
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

from flask import session, flash, session


class Claim:

    def __init__(self, data):
        self.id = data['id']
        self.date_service = data['date_service']
        self.service_type = data['service_type']
        self.charge = data['charge']
        self.vet_name = data['vet_name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.pet = None

    @classmethod
    def createClaim(cls, data):

        query = "INSERT INTO claims (date_service, service_type, charge, vet_name, description, pet_id, user_id, created_at, updated_at) VALUES(%(date_service)s, %(service_type)s, %(charge)s, %(vet_name)s, %(description)s, %(pet_id)s, %(user_id)s, NOW(), NOW());"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        claim_id = result

        return claim_id

    @classmethod
    def get_claim_by_id(cls, id):

        data = {
            'id': id
        }

        query = "SELECT * FROM claims WHERE id = %(id)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        if result:
            result = cls(result[0])
        return result

    @classmethod
    def get_all_claims(cls, id):

        claims = []

        data = {
            'id': id
        }

        query = "SELECT * FROM claims LEFT JOIN pets ON claims.pet_id = pets.id WHERE claims.user_id = %(id)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)
        if result:

            for row in result:

                claim = cls(row)

                data = {
                    'id': row['pets.id'],
                    'pet_name': row['pet_name'],
                    'birthday': row['birthday'],
                    'breed': row['breed'],
                    'created_at': row['pets.created_at'],
                    'updated_at': row['pets.updated_at'],
                    'user_id': row['pets.user_id']

                }
                claim.pet = pet.Pet(data)
                claims.append(claim)

        return claims

    @classmethod
    def viewClaim(cls, id):

        data = {
            'id': id
        }

        query = "SELECT * FROM claims LEFT JOIN pets ON claims.pet_id = pets.id WHERE pet_id = %(id)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        print(result)
        if result:
            result = result[0]

        return result

    @classmethod
    def get_claim_to_edit(cls, id):

        data = {
            'id': id
        }

        query = "SELECT * FROM claims LEFT JOIN pets ON claims.pet_id = pets.id WHERE claims.id = %(id)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)
        if result:
            result = result[0]

        return result

    @classmethod
    def editClaim(cls, data):

        query = "UPDATE claims SET date_service = %(date_service)s, service_type = %(service_type)s, charge = %(charge)s, vet_name = %(vet_name)s, description = %(description)s WHERE id = %(id)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        return result

    @classmethod
    def deleteClaim(cls, id):

        data = {
            'id': id
        }
        query = "DELETE FROM claims WHERE id = %(id)s;"

        result = connectToMySQL('Pet_Insurance').query_db(query, data)

        return result
