# S.discard()  --> removes only specified data like remove method.

s1 = {60,120,180,240}


s1.discard(180)
print(s1)

#{120, 240, 60}  
#  and it doesn't gives error when the element is not specified.

s1 = {60,120,180,240}


s1.discard()
print(s1)
