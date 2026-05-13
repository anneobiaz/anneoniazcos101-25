from Account import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02, withdraw_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal of ${amount} rejected. Limit is ${self.withdraw_limit}.")
        else:
            super().withdraw(amount)

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} applied.")



print("--- Savings Account ---")
saving = SavingsAccount("Alice", 200)

saving.withdraw(150)
saving.apply_interest()
