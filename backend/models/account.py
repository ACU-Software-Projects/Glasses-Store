class Account:
    def __init__(self, accountId, name, email, password, balance):
        self.accountId = accountId
        self.name = name
        self.email = email
        self.password = password
        self.balance = balance

    def login(self):
        # Placeholder for login functionality
        pass

    def logout(self):
        # Placeholder for logout functionality
        pass

    def editAccountDetails(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")
