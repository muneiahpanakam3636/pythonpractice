class Test:
    def __init__(self):
        self.a = 100
    def m1(self):
        self.b = 200  
    @classmethod
    def m2(cls):
       self.d=400
t1 =Test()
t2 =Test()
t1.m1()
t2.c= 300
t1.m2()
t2.m2()
print(t1.__dict__)
print(t2.__dict__)


#  t1.m2()
#   File "D:\python\PART-3\OOP-2\Class variable\four.py", line 8, in m2
#     self.d=400
#     ^^^^
# NameError: name 'self' is not defined