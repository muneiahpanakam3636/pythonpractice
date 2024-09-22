# a= int(input("Enter first no:"))
# b= int(input("Enter Second no:"))

# print(a/b)
# print("GM")

#ValueError: invalid literal for int() with base 10: 'ten'.by using try and except we can overcome.


try:
    a= int(input("Enter first no:"))
    b= int(input("Enter Second no:"))
except:

    print(a/1)
print("GM")
#10.0
#GM