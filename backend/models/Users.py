from Cart import Cart
import account
class User(account.Account):
    def __init__(self, contactInfo,accountId, name, email, password, balance):
        super().__init__(accountId, name, email, password, balance)
        self.contactInfo = contactInfo
        self.cart = Cart(self.contactInfo)

    def viewInvoices(self):
        # This function should return a list of invoices. For simplicity, we'll return an empty list.
        return []

    def initiateReturn(self, productId):
        # This function should initiate a return process. For simplicity, we'll return True.
        return True

    def addProductToCart(self, product):
        self.cart.addItem(product)

