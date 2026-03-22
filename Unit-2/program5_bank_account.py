class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current balance:", self.balance)


account = BankAccount(12345, 1000)

account.deposit(500)
account.withdraw(300)
account.check_balance()
