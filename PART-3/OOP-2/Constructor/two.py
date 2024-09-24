class Test:
    def __init__(self) :
        print("TESt class -- CM")
    def m1(self):
        print("test class -- Im")    
    @classmethod    
    def m2(cls):
        print("test class -- class name")
    @staticmethod    
    def m3():
        print("test class -- static method")

t1 = Test()
t2 = Test()
t1.m1()
t1.m1()
t1.m1()
t1.m1()