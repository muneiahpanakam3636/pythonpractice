def outer():
    print("outer function")
    def inner():
        print("inner function")
    return inner

#inner()    
outer()

#     inner()
#     ^^^^^
# NameError: name 'inner' is not defined. Did you mean: 'iter'?