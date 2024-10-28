import csv

fp = open('emp.csv','r')
rows = csv.reader(fp)

users =list(rows)
print(users)

 #  we are doing slicing
for user_data in users[1:]:
    print(user_data[1])
