from pprint import PrettyPrinter

printer = PrettyPrinter(sort_dicts=False)


class User():
    def __init__(
            self,
            first_name,
            last_name,
            age,
            city,
            state,
            country,
            cell_phone_number,
            email,
            password,
            database
    ):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__city = city
        self.__state = state
        self.__country = country
        self.__cell_phone_number = cell_phone_number
        self.__email = email
        self.__password = password
        self.__database = database

    def insert_user(self):
        data = {
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "age": self.__age,
            "city": self.__city,
            "state": self.__state,
            "country": self.__country,
            "cell_phone_number": self.__cell_phone_number,
            "email": self.__email,
            "password": self.__password,
        }

        # Verificação paar ver se o usuário que será inserido já se encontra na
        # base de dados. Se já estiver cadastrado, a inserção não é feita e é
        # retornado uma mensagem para o usuário.
        query = self.__database.user.count_documents(data)
        if query == 0:
            self.__database.user.insert_one(data)
        else:
            return f"user {data['first_name']} {data['last_name']} \
already entered"

    def list_all_users(self):
        list_of_users = self.__database.user.find()

        for users in list_of_users:
            printer.pprint(users)

    def list_one_user(self, first_name, last_name):
        user = self.__database.user.find_one(
            {
                "first_name": first_name,
                "last_name": last_name
            }
        )

        return user

    def find_user_by_id(self, user_id):
        from bson.objectid import ObjectId

        _id = ObjectId(user_id)

        _user = self.__databse.user.find_one(
            {
                "_id": _id
            }
        )

        return _user

    def update_one_user(self, user_id):
        from bson.objectid import ObjectId

        _id = ObjectId(user_id)

        new_user = {
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "age": self.__age,
            "city": self.__city,
            "state": self.__state,
            "country": self.__country,
            "cell_phone_number": self.__cell_phone_number,
            "email": self.__email,
            "password": self.__password
        }

        self.__database.user.replace_one({"_id": _id}, new_user)

    def remove_user_by_id(self, user_id):
        from bson.objectid import ObjectId

        _id = ObjectId(user_id)

        self.__database.user.delete_one({"_id": _id})

    def remove_all_users(self):
        self.__database.user.delete_many({})

    def list_users_by_range_age(self, min_age, max_age):
        query = {
            "$and": [
                {"age": {"$gte": min_age}},
                {"age": {"$lte": max_age}}
            ]
        }
        users = self.__database.user.find(query).sort("age")

        for user in users:
            return user
