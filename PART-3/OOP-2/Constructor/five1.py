class Account:
    min_bal =500
    def __init__(self,id,name,amount) :
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def deposite(self,amount):
        self.acc_bal = self.acc_bal +amount    


print(Account.__dict__)
print(Account.__dict__)
print(Account.__dict__)