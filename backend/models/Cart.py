from datetime import date


class Cart:
    def __init__(self, userId):
        self.userId = userId
        self.items = []
        self.totalQuantity = 0
        self.totalPrice = 0.0
        self.createdDate = date.today()

    def addItem(self, product):
        self.items.append(product)
        self.totalQuantity += 1
        self.totalPrice += product.price

    def removeItem(self, productId):
        for product in self.items:
            if product.productId == productId:
                self.items.remove(product)
                self.totalQuantity -= 1
                self.totalPrice -= product.price
                break

    def calculateTotalPrice(self):
        self.totalPrice = sum(product.price for product in self.items)

    def clearCart(self):
        self.items = []
        self.totalQuantity = 0
        self.totalPrice = 0.0

    def getCartDetails(self):
        return {
            'userId': self.userId,
            'items': [product.__dict__ for product in self.items],
            'totalQuantity': self.totalQuantity,
            'totalPrice': self.totalPrice,
            'createdDate': self.createdDate
        }
