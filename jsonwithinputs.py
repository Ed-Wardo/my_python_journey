import requests

request = requests.get("https://reqres.in/api/users?page=2")
dados = request.json()
users = dados["data"]
email = dados["data"]
id = dados["data"]

prompt1 = input("Você quer emails, nomes ou id? ")


if prompt1 == "nomes":
    for user in users:
        print((f"Nome: {user ["first_name"]}"), (f"{user ["last_name"]}"))

elif prompt1 == "emails":
    for user in users:
        print (f"Email: {user ["email"]}")
        
elif prompt1 == "id":
    for user in users:
        print (f"id: {user ["id"]}")
