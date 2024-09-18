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

print(emp_dict)