class Account:

    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
        print('inside Account class constructor')
    def open_Account(self):
        print('account opened')
a1 = Account(101,"rahul",6000)            
a2 = Account(102,"sonia",000)    

a1.open_Account()
a2.open_Account()
a1.open_Account()
a2.open_Account()
        