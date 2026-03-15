class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return f"{self.__owner}: {self.__balance}"

a1 = BankAccount("Ivan", 100)
a2 = BankAccount("Olena", 500)
a3 = BankAccount("Petro", 1000)

a1.deposit(50)
a1.withdraw(30)
print(a1.get_balance())

a2.deposit(200)
a2.withdraw(100)
print(a2.get_balance())

a3.withdraw(500)
a3.deposit(100)
print(a3.get_balance())