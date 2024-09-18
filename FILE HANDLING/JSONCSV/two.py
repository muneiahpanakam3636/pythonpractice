import json
emp_dict={'eid': '101', 'ename': 'Rahul', 'avail': True, 'loc': 'undefined', 'esal': None}


print(emp_dict)
print(type(emp_dict))
emp_json = json.dumps(emp_dict)

print(emp_json)
print(type(emp_json))