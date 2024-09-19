import json
#import csv
customers = [
    {'id':101,'name':'Rahul','avila':True},
    {'id':102,'name':'sonia','avila':False},
    {'id':103,'name':'Priya','avila':False},
]

fp1 =open('emp.json','w')
#fp2 =open('emp.csv','w')

json.dump(customers,fp1)
print('NEW JSON File Created successfully')

fp1.close()