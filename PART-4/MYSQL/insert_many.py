import mysql.connector

mycurser = None

try:
   dbcon = mysql.connector.connect(host = "localhost",user="root",password="root",database = "8pm")
   mycurser=dbcon.cursor()
   sql_stm = '''insert into employee values(%s,%s,%s,%s)'''
   data = [(102,"sonia",55000.00,"chennai"),
           (103,"priya",65000.00,"delhi"),
           (104,"modi",75000.00,"varanasi"),
           (105,"muni",85000.00,"tirupati"),
           (106,"modi",75000.00,"puttur"),
           (107,"modi",75000.00,"nellore")
           ]
   mycurser.executemany(sql_stm,data)
   dbcon.commit()
   print("all are inserted")
           
except mysql.connector.DatabaseError as err:
   if err:
      print(err)
finally:
   mycurser.close()
   dbcon.close()         