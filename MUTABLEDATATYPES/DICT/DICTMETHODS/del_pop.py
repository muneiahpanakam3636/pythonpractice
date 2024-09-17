emp ={
    'eid':101,
    'ename':"Rahul",
    'esal':45000.90
}

# emp.pop()
# print(emp)#TypeError: pop expected at least 1 argument, got 0

emp.pop('ename')
print(emp)
#{'eid': 101, 'esal': 45000.9}