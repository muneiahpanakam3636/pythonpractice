# import json
import csv
customers = [
    {'id':101,'name':'Rahul','avila':True},
    {'id':102,'name':'sonia','avila':False},
    {'id':103,'name':'Priya','avila':False},
]

#fp1 =open('emp.json','w')
fp2 =open('emp.csv','w',newline='')

wr=csv.writer(fp2)
wr.writerow(['id','name','avial'])
for cust in customers:
    wr.writerow([cust['id'],cust['name'],cust['avila']])

print('NEW CSV File Created successfully')

#fp1.close()
fp2.close()