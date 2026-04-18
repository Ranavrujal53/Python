from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "Using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "Using UPI Payment")


method = input("Enter the payment method (card/upi): ").lower()
amount = int(input("Enter the amount: "))

if method == "card":
    obj = CreditCard()
elif method == "upi":
    obj = UPI()
else:
    print("Invalid payment method!")
    exit()

obj.pay(amount)