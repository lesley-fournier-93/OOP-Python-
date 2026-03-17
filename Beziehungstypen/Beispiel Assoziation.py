class Person:
    def __init__(self, name):
        self.vorname = name
        self.nachname = ""
        self.alter = 44

class BankAccount:
    def __init__(self, balance):
        self.balance = balance


class Customer:
    def __init__(self, person):
        self.name = person.vorname
        self.customer_alter = person.alter
        self.account = None

    def open_account(self, balance):
        self.account = BankAccount(balance)

    def deposit(self, amount):
        self.account.balance += amount

    def withdraw(self, amount):
        if amount > self.account.balance:
            raise ValueError('Insufficient funds')
        self.account.balance -= amount

p1 = Person('Alice')
c1 = Customer(p1)
c1.open_account(1000)
c1.deposit(500)
c1.withdraw(200)
print(c1.account.balance)


