class Account():
    def __init__(self,balance,accno):
        self.balance=balance
        self.account=accno
        
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("final balance is :",self.get_balance())
            
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")
        print("final balance is :",self.get_balance())
        
    def get_balance(self):
        return self.balance
a1=Account(23,3298219)
a1.debit(1000)
a1.credit(2000)
print(a1.balance,a1.account )