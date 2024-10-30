import json
import csv
fp1=open('emp.json','r')

users=json.load(fp1)

 
print(users)

female_users=list(filter(lambda user:user['gender']=="Female",users))
fp2=open('emp.csv','w',newline='') 
csv_obj=csv.DictWriter(fp2,fieldnames=female_users[0].keys())
csv_obj.writeheader()
csv_obj.writerows(female_users)


print(csv_obj)

fp1.close()
fp2.close()