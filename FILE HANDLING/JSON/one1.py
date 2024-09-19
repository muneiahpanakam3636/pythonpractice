import json

emp_json = '''{
"id":101,
"name":"Rahul",
"avila":true,
"loc":"undefined",
"sal":null
}'''

print(emp_json)
print(type(emp_json))

emp_dict = json.loads(emp_json)
print(emp_dict)

print(type(emp_dict))