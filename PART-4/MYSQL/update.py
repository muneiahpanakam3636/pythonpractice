import mysql.connector

mycursor = None
try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database ="8pm")
    mycursor=dbcon.cursor()
    mycursor.execute('select *from employee')
    empdata =mycursor.fetchall()
    for emp in empdata:
        print('EmployeeID:',emp[0],"EmployeeName:",emp[1],"EmployeeSal:",emp[2],"EmployeeLoc:",emp[3])
except mysql.connector.DatabaseError as err:
    if err:
        print(err)    

finally:
    mycursor.close()
    dbcon.close()        