class Account():

    def __init__(self, name, initial_balance=0):
        # Constructor initializes an Account object with a given name and optional initial_balance (default is 0).
        self.name = name
        self.balance = initial_balance

    def get_name(self):
        # Getter method for retrieving the account holder's name.
        return self.name

    def get_balance(self):
        # Getter method for retrieving the current account balance.
        return self.balance

    def deposit(self, amount):
        # Method to deposit a specified amount into the account.
        self.balance += amount
        print(f'Deposit accepted: {amount}, available balance: {self.balance}')

    def withdraw(self, amount):
        # Method to withdraw a specified amount from the account.
        if self.balance < amount:
            # Check if withdrawal amount exceeds the available balance.
            print(f'Unable to withdraw. Insufficient funds. Available balance: {self.balance}')
        else:
            # Withdrawal successful; update the balance.
            self.balance -= amount
            print(f'Withdrawal successful. Available balance: {self.balance}')