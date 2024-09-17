

emp={'name': 'Rahul gandhi'}
# emp.update('eid',101)
print(emp)  # update expected at most 1 argument, got 2
#  and it is over come by this...
emp.update({'eid':101})
print(emp)
#{'name': 'Rahul gandhi', 'eid': 101}