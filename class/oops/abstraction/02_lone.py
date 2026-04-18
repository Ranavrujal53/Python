
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        self.balance = 0

    @abstractmethod 
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        print(f"Current balance is {self.balance}")


# 🔹 Saving Account
class SavingAccount(Account):

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")


# 🔹 Loan Account
class LoanAccount(Account):

    def deposit(self, amount):
        self.balance -= amount   # paying loan
        print(f"Loan repaid: {amount}")

    def withdraw(self, amount):
        self.balance += amount   # taking loan
        print(f"Loan taken: {amount}")


# 🔥 Create Loan Account Object
loan = LoanAccount()

loan.get_balance()
loan.withdraw(10000)   # take loan
loan.get_balance()
loan.deposit(15000)     # repay loan
loan.get_balance()