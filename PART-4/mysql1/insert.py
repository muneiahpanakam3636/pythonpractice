import mysql.connector
mycursor =None

try:
    dbcon =mysql.connector.connect(host="localhost",user="root",password="root",database="9pm")
    mycursor=dbcon.cursor()
    sql_stm='''insert into employee values(101,"kajal",65000.00,"hyderabad")'''
    mycursor.execute(sql_stm)
    dbcon.commit()
    print("inserted successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)
finally:
    dbcon.close()
    mycursor.close()