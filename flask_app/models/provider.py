from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL


class Provider:

    def __init__(self, data):
        self.id = data['id']
        self.office_name = data['office_name']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_providers(cls):

        query = "SELECT * FROM providers;"

        result = connectToMySQL('providers').query_db(query)

        return result
