import mysql.connector
mycursor = None

try:
    dbcon = mysql.connector.connect(host ="localhost",user = "root",password = "root",database ="8pm" )
    mycursor =dbcon.cursor()
    mycursor.execute('select * from employee')
    empdata = mycursor.fetchall()
    for emp in empdata:
        print(emp)
except mysql.connector.DatabaseError as err:
    if err:
        print("unable to connect database")    
finally:
    mycursor.close()
    dbcon.close()
