##S.remove()--> remooves only specified data
s1 = {20,40,60,80}
s1.remove(60)
print(s1)



#{40, 80, 20}   removes specified data only
#  and it gives error when the element is not specified

s1 = {20,40,60,80}
s1.remove()
print(s1)
#TypeError: set.remove() takes exactly one argument (0 given)