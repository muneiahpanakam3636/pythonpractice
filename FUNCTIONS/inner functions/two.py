#  how to involke inner function   in outside----by usingreturn the function reference  


def outer():
    print("outer function")
    def inner():
        print("inner function")
    return inner    
inner =outer()
inner()
inner()

# outer function
# inner function
# inner function