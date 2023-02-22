from connection import Database
from user import User

# Instânciando a classe Database.
banco = Database()

# Criando uma lista de dicionários para popular o banco de dados.
user_data = [
    {
        "first_name": "Scott",
        "last_name": "McGall",
        "age": 17,
        "city": "Kent",
        "state": "Ohio",
        "country": "USA",
        "cell_phone_number": "9836621",
        "email": "mcgall.scott@email.com",
        "password": "762scott",
    },
    {
        "first_name": "Tom",
        "last_name": "Riddle",
        "age": 46,
        "city": "Dallas",
        "state": "Texas",
        "country": "USA",
        "cell_phone_number": "129621",
        "email": "riddle@email.com",
        "password": "SnakeSli",
    }
]

# Laço para desempacotar a lista com dicionários e associar a cada
# atributo da classe User.
for datas in user_data:
    # Passando os dados da classe Database por meio de composição.
    us = User(
        datas["first_name"],
        datas["last_name"],
        datas["age"],
        datas["city"],
        datas["state"],
        datas["country"],
        datas["cell_phone_number"],
        datas["email"],
        datas["password"],
        banco
    )

    # Chamando o método que adiciona os dados do usuário na Database.
    # printer.pprint(us.insert_user())  # Descomente para executar esse trecho.

# Dados para atualizar o usuário.
new_user = [
    {
        "first_name": "Tom",
        "last_name": "Riddle",
        "age": 46,
        "city": "Dallas",
        "state": "Texas",
        "country": "USA",
        "cell_phone_number": "129621",
        "email": "riddle@email.com",
        "password": "SnakeSli",
    }
]

for datas in new_user:
    us = User(
        datas["first_name"],
        datas["last_name"],
        datas["age"],
        datas["city"],
        datas["state"],
        datas["country"],
        datas["cell_phone_number"],
        datas["email"],
        datas["password"],
        banco
    )

# Atualizando o usuário com o id.
# us.update_one_user("INSIRA O ID")  # Retire o # para executar o comando.

# Listando todos os usuários do banco de dados.
# us.list_all_users()

# Removendo todos os usuários do banco de dados.
# us.remove_all_users()
