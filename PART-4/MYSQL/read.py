
import mysql.connector
mycursor = None

try:
    dbcon = mysql.connector.connect(host="localhost",user = "root",password="root",database="8pm")
    
    mycursor = dbcon.cursor()
    mycursor.execute('select eid,ename from employee')
   
    empdata =mycursor.fetchall()
    for emp in empdata:
        print(emp)

except mysql.connector.DatabaseError as error:
    if error:
        print(error)
finally:
   
    mycursor.close()
    dbcon.close()