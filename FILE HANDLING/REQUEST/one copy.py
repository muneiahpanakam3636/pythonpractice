import requests

data=requests.get('https://dummyjson.com/users')

user_data = data.json


print(type(user_data))

