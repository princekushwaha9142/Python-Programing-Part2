# Encapsulation means protecting data from outside access.
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
