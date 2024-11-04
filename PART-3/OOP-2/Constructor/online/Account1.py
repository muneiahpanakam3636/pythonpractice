class Account:
    min_bal = 500
    def __init__(self,id,name):
        self.id = id   
        self.name = name   
    def open_Account(self):
        self.acc_bal=200
    @classmethod
    def get_min_bal(cls):
        pass
    @staticmethod
    def cal_interest():
        tax = 5    

a1 =Account(101,'rahul')    
a2 =Account(102,'sonia')   
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)