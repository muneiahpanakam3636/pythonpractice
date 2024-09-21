try:
    a = int(input("Enter First no:"))
    b =int(input("Enter Second no:"))
    print(a/b)
except ZeroDivisionError as e:
    print("can't divide zero")
except ValueError as e:
    print("can't convert str to int" )        