#This is a Object-Oriented Programming project to create a Bank Account.

class BankAccount:
    #Initializing the class
    def __init__(self):
        self.balance = 0

    #this function will take deposit amount
    def deposit(self, amount)
        #balance amount is updated after depositing
        self.balance = self.balance + amount

    def withdraw(self, amount):
        #it takes the amount you withdraw as an argument
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def print_balance(self):
        return self.balance
        

account = BankAccount() #creating an instance object
account.deposit(100) #Depositing 100 dollars
account.deposit(50)
print(account.print_balance)
