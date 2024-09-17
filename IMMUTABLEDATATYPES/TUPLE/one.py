# 1)Tuple is a group of element as one entity
# 2)where allowed duplicates & heterogeneous elements
# 3)index is possible  -ve & +ve 
# 4)once tuple object is created ,we cant perform any update & delete operation(read only object/read only version of list )
# 5)insertion is maintained/order guarentee
# 6)how to accessing - indexing.


    #create                                  read
# t1 = (10,20,30,40)                         t1.count()
# t2 = t1.copy()                             t1.index()
                                            

t1 = ()
t2 = 10,
t3 = 10,20,30,40,50
t4 =(10,20,30,40)
t5 = tuple(range(10))

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))
print(type(t5))