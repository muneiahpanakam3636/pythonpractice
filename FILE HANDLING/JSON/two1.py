import json

emp_dict ={'id': 101, 'name': 'Rahul', 'avila': True, 'loc': 'undefined', 'sal': None}

print(emp_dict)

print(type(emp_dict))

emp_json =json.dumps(emp_dict)

print(emp_json)
print(type(emp_json))