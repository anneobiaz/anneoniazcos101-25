from Account import Account

class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        available_balance = self.get_balance() + self.overdraft_limit
        if amount <= available_balance:
            print(f"Withdrawal of ${amount} approved (using overdraft if necessary)")
        else:
            print(f"Withdrawal of ${amount} rejected (exceed overdraft limit)")

print("\n --- Current Account ---")
current = CurrentAccount("Bob", 100)
current.withdraw(400)
