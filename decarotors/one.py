def outer():
    print("outer function")
    def inner():
        print("ineer function")

    inner()
    inner()
outer()    


# outer function
# ineer function
# ineer function