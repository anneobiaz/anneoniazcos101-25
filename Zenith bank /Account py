class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposit {amount} from {self.__balance}")
        else:
            print("Invalid deposit amount ")

    def withdraw(self, amount):
        """Base withdraw method to be over ridden (Polymorphism)"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw {amount} from {self.__balance}")
        else:
            print("Invalid withdrawal amount ")

    def get_balance(self):
        """public getter for the private balance"""
        return self.__balance
