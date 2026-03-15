# Create Payment System

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print(f"Processing credit card payment of {amount}")

class UPI(Payment):

    def pay(self, amount):
        print(f"Processing UPI payment of {amount}")

class PayPal(Payment):

    def pay(self, amount):
        print(f"Processing PayPal payment of {amount}")

payment_method = input("Enter payment method (creditcard/upi/paypal): ").lower()
amount = float(input("Enter amount to pay: "))
if payment_method == "creditcard":
    payment = CreditCard()
elif payment_method == "upi":
    payment = UPI()
elif payment_method == "paypal":
    payment = PayPal()
else:
    print("Invalid payment method.")
    exit()

payment.pay(amount)

