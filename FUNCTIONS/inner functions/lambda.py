#  nameless function is called as LAMBDA(lambda).

# def add (x):
#     return x+1
# r1 = add(100)
# print(r1)
#101

#  it will written as below

add = lambda x:x+1
r1 =add(100)
print(r1)
#101
print(type(r1))
print(type(add))

# 101
# <class 'int'>
# <class 'function'>