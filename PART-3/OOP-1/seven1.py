class Account:
    acc_bal=0
    def deposite_amount(self,amount):
        self.acc_bal = self.acc_bal+amount
a1 = Account()        
a2 = Account()        
print(a1.__dict__)
print(a2.__dict__)

a1.deposite_amount(5000)
a1.deposite_amount(1000)


print(a1.__dict__)
print(a2.__dict__)