import json
fp=open('emp1.json','r')
emp_dict=json.load(fp)

print(emp_dict)
# only id

for emp in emp_dict:
    print(emp['id'])