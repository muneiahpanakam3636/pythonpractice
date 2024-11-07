import mysql.connector
mycursor =None

try:
    dbcon=mysql.connector.connect(host="localhost",user ="root",password="root",database="8pm")
    mycursor=dbcon.cursor()
    sql_stm='''delete from employee where eid=101'''
    mycursor.execute(sql_stm)
    dbcon.commit()
    print("deleted successfully")
except mysql.connector.DatabaseError as error:
    if error:
        print(error)

finally:
    mycursor.close()
    dbcon.close()