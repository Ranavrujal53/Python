from abc import ABC,abstractmethod

class Account(ABC):

    balance = 0
    @abstractmethod 
    def deposties(self,amount):
        pass
    @abstractmethod
    def withdrow(self,amount):
        pass

    def get_balance(self):
        print(f"Current balance is {self.balance}")

class savingAccount(Account):
    def deposties(self, amount):
        self.balance += amount

    def withdrow(self, amount):
        if amount>self.balance:
            print("Insufficient balance!")

        else:
            self.balance -= amount
            # print(f"Withdrawn: {amount}")

# a = savingAccount()

# a.get_balance()
# a.deposties(5000)
# a.deposties(2000)
# a.get_balance()
# a.withdrow(150)
# a.get_balance()

class loneAccount(Account):
    def deposties(self, amount):
        if amount>self.balance:
            amt = amount - self.balance
            print(f"you have left{amt}")
            self.balance=0

        else:
            self.balance -= amount

    def withdrow(self, amount):
        self.balance+= amount
l = loneAccount()

l.get_balance()
l.withdrow(5000)
l.get_balance()
l.deposties(3000)
l.get_balance()