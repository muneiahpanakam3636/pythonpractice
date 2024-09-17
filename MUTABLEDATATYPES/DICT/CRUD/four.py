#LIST & TUPLE are allowed duplicate elements
# set is not allowed duplicates
#DICT is not allowed duplicate keys

emp ={
    'eid ':101,
    'eid ':102,#{'eid ': 102, 'eid': 104}    - here variation in elements is avilable  so printing 2 ids
    'eid':103,
    'eid':104
}
print(emp)

emp = {
     'eid':101,
     'eid':102,
     'eid':103,    #{'eid': 104}  - here variation is not there so printing only one id
     'eid':104
}
print(emp)