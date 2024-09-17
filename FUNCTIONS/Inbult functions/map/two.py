#  map is doing executing the provided function for every element of your sequence

def addplus (mark):
    return mark+1
marks = [35,15,10]

#map (function,seq)
obj = map(addplus,marks)
print(type(obj))
print(list(obj))

# <class 'map'>
# [36, 16, 11] 