class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Wpłacono {amount}. Nowy stan konta: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Brak środków na koncie!"
        self.balance -= amount
        return f"Wypłacono {amount}. Nowy stan konta: {self.balance}"

konto = BankAccount(100)
print(konto.deposit(50))
print(konto.withdraw(200)) 
