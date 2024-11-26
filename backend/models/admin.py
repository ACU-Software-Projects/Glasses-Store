import account


class Admin(account.Account):
    def __init__(self, role, accountId, name, email, password, balance):
        super().__init__(accountId, name, email, password, balance)
        self.role = role

    def add_product(self, product):
        # Placeholder for adding product functionality
        pass

    def update_product(self, productId, details):
        # Placeholder for updating product functionality
        pass

    def remove_product(self, productId):
        # Placeholder for removing product functionality
        pass

    def view_all_invoices(self):
        # This function should return a list of all invoices. For simplicity, we'll return an empty list.
        return []

    def manage_user_accounts(self, userId, action):
        # Placeholder for managing user accounts functionality
        pass
