class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def Deposit(self, amount):

        self.balance = self.balance + amount
    
    def Withdraw(self, amount):

        if self.balance < amount:
            print ('You don`t have enough money in your account')
        else:
            self.balance = self.balance - amount
    
    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"

acct1 = Account("Marcell", 100000)

acct1.Deposit(30000)
acct1.Withdraw(10000)
print(acct1)