from abc import *

class Bank(ABC):
    def cal_tax(self):
        pass
b= Bank()

print(b)
print(id(b))
print(b.__dict__)