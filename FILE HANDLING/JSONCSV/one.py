
#json.loads()
#  convert json data into python obj.

# json.dumps()
# convertb python data into json type




import json

emp_json = '''{
"eid":101,
"ename":"Rahul",
"availa":true,
"loc":"undefined",
"esal":null
}'''

print(emp_json)
emp_dict = json.loads(emp_json)
print(type(emp_dict))
print(emp_dict)