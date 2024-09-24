class Test:
    def __init__(self) :
        print("test class --CM")
    def m1(self):
        print("test class --IM")
    @classmethod
    def m2(self):
      print("test class --ClassMethod") 
    @staticmethod       
    def m3(self):
        print("test class--Static method")       
t1 = Test()     
t2 = Test()     
t1.m1()
t1.m1()
t1.m1()
t1.m2()
t1.m2()