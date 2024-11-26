import Cart as cart

class User:
    def __init__(self, contactInfo):
        self.contactInfo = contactInfo
        self.cart = cart(self.contactInfo)

    def viewInvoices(self):
        # This function should return a list of invoices. For simplicity, we'll return an empty list.
        return []

    def initiateReturn(self, productId):
        # This function should initiate a return process. For simplicity, we'll return True.
        return True

    def addProductToCart(self, product):
        self.cart.addItem(product)

