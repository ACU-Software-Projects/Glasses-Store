class Invoice:
    def __init__(self, invoiceId, userId, productList, totalAmount, issueDate, status):
        self.invoiceId = invoiceId
        self.userId = userId
        self.productList = productList
        self.totalAmount = totalAmount
        self.issueDate = issueDate
        self.status = status
