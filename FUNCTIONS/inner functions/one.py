#  what is a inner function?
#  how to involke inner function   in outside----by usingreturn the function reference  


def outer():
    print("outer function")
    def inner():
        print("inner function")
    return 100    
      
value =outer()
print(value)
#outer function
#100   
    
        


