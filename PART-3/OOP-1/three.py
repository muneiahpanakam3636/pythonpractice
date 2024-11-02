class Account:
    '''Account class is created'''
    min_bal = 500
    def open_Account(self):
        
       print('Account created succssfully')
    @classmethod   
    def m2(cls):
        pass
    @staticmethod 
    def m3():
        pass 
a1 = Account()
a2 = Account()
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)
# what class contains : variables and methods.//self:  is a pointer ;pointing to current obj.
