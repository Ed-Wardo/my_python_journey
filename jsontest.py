import requests

url = ("https://reqres.in/api/users")
data = {
    "name": "Eduardo",
    "job": "developer",
    "id": "001"
}

request = requests.post(url, data)
print(request.json())
