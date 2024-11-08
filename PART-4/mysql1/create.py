import mysql.connector

mycursor =None
try:
    dbcon = mysql.connector.connect(host="localhost",user="root",password="root",database="9pm")
    mycursor=dbcon.cursor()
    sql_stm = '''create table employee(
               eid int,
               ename varchar(32),
               esal float,
               eloc varchar(32)
               );'''
    mycursor.execute(sql_stm)
    dbcon.commit()
    print("created successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)   

finally:
    mycursor.close()
    dbcon.close()         