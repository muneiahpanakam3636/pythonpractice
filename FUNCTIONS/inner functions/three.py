def outer():
    print("outer function")
    def inner():
        print("inner function")
    return 1000    
      
value =outer()
print(value)

#outer function
#1000