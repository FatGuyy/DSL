# Write a python program that computes the net amount of a bank
# account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100 W 200 (Withdrawal is not allowed if balance is going
# negative. Write functions for withdraw and deposit) D means deposit
# while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300 , D 300 , W 200 , D 100 ,
# Then, the output should be: 500
# ''')

# computes net bank amount based on the input
# "D" for deposit, "W" for withdrawal 

class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):  
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()

