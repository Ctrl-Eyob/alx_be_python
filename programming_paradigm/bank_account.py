class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance   # encapsulated attribute

    def deposit(self, amount):
        """Deposit a positive amount to the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw an amount if sufficient balance exists."""
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance}")