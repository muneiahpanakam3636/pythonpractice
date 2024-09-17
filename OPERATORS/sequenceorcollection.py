# what is sequence/collection?
#list,string,set,tuple,dict

l1 = [10,20,30,40,50]
t1 = (10,20,30,40,50)
s1 ={10,20,30,40,50}
str1 = 'raani'
dict ={'id':101,'name':'radha'}

r =range(10,20)

b = bytes(l1)
ba = bytearray(l1)
fs = frozenset(s1)
# print(10 in l1)
# print(20 in t1)
# print(30 in s1)
# print('a' in str1)
# print('name' in dict)
print('a' not in str1 )
print(10 not in l1)
print(11 in r)
print(60 in ba)


