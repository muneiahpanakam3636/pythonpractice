emp ={
    'eid':101
}
value = emp.setdefault('eid',102)  # duplicate key is present ,no change
value = emp.setdefault('extra_eid',102)#  a new key is came, it will add.
print(value)
print(emp)

# 102
# {'eid': 101, 'extra_eid': 102}