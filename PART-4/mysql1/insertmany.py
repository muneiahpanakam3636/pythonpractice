import mysql.connector
mycursor =None

try:
    dbcon =mysql.connector.connect(host="localhost",user="root",password="root",database="9pm")
    mycursor=dbcon.cursor()
    sql_stm='''insert into employee values(%s,%s,%s,%s)'''
    data = [(102,"sreeleela",55000.00,"banglore"),
           (103,"kavya",45000.00,"punjab"),
           (104,"pooja",35000.00,"Mumbai"),
           (105,"samatha",25000.00,"chittor"),
           (106,"divya",15000.00,"chennai")
           ]
    
    mycursor.executemany(sql_stm,data)
    dbcon.commit()
    print("All are inserted successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)
finally:
    dbcon.close()
    mycursor.close()