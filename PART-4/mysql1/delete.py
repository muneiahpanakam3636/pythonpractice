import mysql.connector
mycursor =None

try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="9pm")
    mycursor = dbcon.cursor()
    sql_stm='''delete from employee where eid=104'''
    mycursor.execute(sql_stm)
    dbcon.commit()
    print("deleted successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)    