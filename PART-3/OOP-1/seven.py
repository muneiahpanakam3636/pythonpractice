class Account:
    acc_bal = 0
    def deposite_amount(self,amount):
        self.acc_bal =self.acc_bal+amount


a1= Account()  #Rahul
a2=Account()  # Sonia

print(a1.__dict__)
print(a2.__dict__)

a1.deposite_amount(5000)
a2.deposite_amount(1000)

print(a1.__dict__)
print(a2.__dict__)