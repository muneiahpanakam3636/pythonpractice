#mockarro.com



#json.loads()
#  convert json data into python obj.

# json.dumps()
# convertb python data into json type

import json

emp_json = """{
    "id":101,
    "name":"Rahul",
    "avila":true,
    "loc":"undefined",
    "sal":null
    }"""


print(emp_json)
print(type(emp_json))

emp_dict = json.loads(emp_json)
print(type(emp_dict))
print(emp_dict)