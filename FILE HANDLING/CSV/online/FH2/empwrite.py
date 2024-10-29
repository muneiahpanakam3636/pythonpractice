import csv

fp=open('user.csv','w',newline='')
csv_obj=csv.writer(fp)
csv_obj.writerow(['name','ID', 'location'])
csv_obj.writerow(['muni', '101', 'tpt'])
csv_obj.writerow(['raju', '102', 'skht'])
csv_obj.writerow(['raani', '103', 'chennai'])

fp.close()
