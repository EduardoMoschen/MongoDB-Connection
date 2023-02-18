import os

from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.__env = load_dotenv(find_dotenv())
        self.__password = os.environ.get("MONGO_DB_PASSWORD")
        self.__uri = "YOUR STRING CONNECTION"
        self.__client = MongoClient(self.__uri)
        self.__database = self.__client.production
        self.user = self.__database.user

    def schema_validation(self):
        self.__user_validator = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": [
                    "first_name",
                    "last_name",
                    "age",
                    "city",
                    "state",
                    "country",
                    "cell_phone_number",
                    "email",
                    "password"
                ],
                "properties": {
                    "first_name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "last_name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "age": {
                        "bsonType": "int",
                        "minimum": 0,
                        "maximum": 150,
                        "description": "must be a integer in [0, 150] and \
is required"
                    },
                    "city": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "state": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "country": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "cell_phone_number": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "email": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "password": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        }
        self.__database.command(
            "collMod", "user", validator=self.__user_validator)
