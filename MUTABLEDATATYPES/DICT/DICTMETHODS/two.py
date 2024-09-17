emp ={
    'eid':101,
    'ename':"Rahul",
    'esal':45000.00,
}
# printing all keys by using for loop

for key in emp.keys():
    print(key)
print("********") 

 # printing all values by using for loop
for value in emp.values():
    print(value)
print("********") 
#  printing keys and values together    
for keys,values in emp.items():
    print(keys,values)

