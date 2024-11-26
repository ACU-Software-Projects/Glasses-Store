from datetime import date

class Product:
    def __init__(self, productId, name, brand, style, description, price, category):
        self.productId = productId
        self.name = name
        self.brand = brand
        self.style = style
        self.description = description
        self.price = price
        self.category = category


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


class Invoice:
    def __init__(self, invoiceId, userId, productList, totalAmount, issueDate, status):
        self.invoiceId = invoiceId
        self.userId = userId
        self.productList = productList
        self.totalAmount = totalAmount
        self.issueDate = issueDate
        self.status = status


class User:
    def __init__(self, contactInfo):
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


class Account(User):
    def __init__(self, accountId, name, email, password, balance):
        super().__init__(email)
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


class Admin:
    def __init__(self, role):
        self.role = role

    def addProduct(self, product):
        # Placeholder for adding product functionality
        pass

    def updateProduct(self, productId, details):
        # Placeholder for updating product functionality
        pass

    def removeProduct(self, productId):
        # Placeholder for removing product functionality
        pass

    def viewAllInvoices(self):
        # This function should return a list of all invoices. For simplicity, we'll return an empty list.
        return []

    def manageUserAccounts(self, userId, action):
        # Placeholder for managing user accounts functionality
        pass
