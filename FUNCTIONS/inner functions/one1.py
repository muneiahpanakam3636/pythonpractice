def outer():
    print("outer function")
    def inner():
        print("inner function")

    return 100
value = outer()

print(value)