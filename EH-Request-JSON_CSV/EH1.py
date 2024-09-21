try:
    a = int(input("enter first number:"))
    b= int(input("enter second number:"))
    print(a/b)

except ZeroDivisionError as e:
    print("can't divide zero") 
except ValueError as e:
    print("can't convert str into int")       