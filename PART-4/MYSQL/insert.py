import mysql.connector
mycurser = None

try :
    dbcon = mysql.connector.connect(host="localhost",user="root",password ="root",database= "8pm")

    mycurser= dbcon.cursor()
    sql_stm ='''insert into employee values(101,"rahul",45000.00,"bengaluru")'''

    mycurser.execute(sql_stm)
    dbcon.commit()
    print(" data inserted successfully")


except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    dbcon.close()    
            
