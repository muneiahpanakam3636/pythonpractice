import csv

fp=open('emp.csv','w',newline='')
csv_obj=csv.writer(fp)
csv_obj.writerow(['eid','ename','esal'])
n=int(input('Enter Number of employees:'))

for i in range(n):
    eid = input('Enter Eid:')
    ename =input('Enter Ename:')
    esal =input('Enter Esal:')

    csv_obj.writerow([eid,ename,esal])

   