import requests

data=requests.get('https://dummyjson.com/users')

print(type(data))

print(type(data.json()))