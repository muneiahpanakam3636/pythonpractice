import json 
fp1 =open('Users.json','r')
users = json.load(fp1)

print(users) 

employees = []

for user in users:
    employees.append({'eid':user['id'],
                      'ename':user['name']
                       })
fp2 = open('emp.json','w')  
json.dump(employees,fp2)


fp1.close()
fp2.close()