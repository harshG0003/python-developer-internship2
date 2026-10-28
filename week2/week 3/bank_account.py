class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Rs. {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: Rs. {self.balance:.2f}")

account = BankAccount("Harsh kumar Saini", 10000)

account.display_balance()
account.deposit(300)
account.withdraw(1000)
account.display_balance()
