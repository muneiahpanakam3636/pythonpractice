import json
emp_json = '''{"eid":101,"ename":"Rahul","esal":45000,"avila":true}'''

emp_obj=json.loads(emp_json)

print(emp_json)
print(emp_obj)