class Banking:
    def __init__(self, account_number, account_name, initial_balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = initial_balance
    
    def deposit(self, account) :
        self.balance += "amount"

    def withdrawal(self, amount):
        if amount > self.amount:
           print ("incufficient funds!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, reciepeint_account):


 