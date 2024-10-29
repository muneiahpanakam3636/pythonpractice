import csv
fp=open('user.csv','w',newline='')
csv_obj=csv.writer(fp)

csv_obj.writerow(['username','emailid','location'])

csv_obj.writerow(['Rahul','Rahul@gmail.com','chennai'])
csv_obj.writerow(['sonia','sonia@gmail.com','noida'])


fp.close()