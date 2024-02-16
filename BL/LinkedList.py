class LinkedList:
    def __init__(self):
        self.head = None
        
    def addToStart(self, data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        print(self.head.product.Id)
        del tempNode
        
    def head(self):
        return self.head
    
    def addToEnd(self, data):
        start = self.head
        tempNode = Node(data)
        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return True
    def checkID(self,item):
        start=self.head
        found=False
        while not found:
            if start.getProduct().Id==item.Id:
                found=True
                return True
            start=start.getNextNode()
        return False
    def remove(self, item):
        start = self.head
        previous = None
        found = False
        while not found:
            if start.getProduct().Id == item.Id:
                found = True
            else:
                previous = start
                start = start.getNextNode()
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found

    # method returns index of the recieved data
    def index(self, data):
        start = self.head
        position = 1

        while start:
            if start.getData() == data:
                return position
            else:
                position += 1
                start = start.getNextNode()
class Node:
    def __init__(self, product=None, link = None):
        self.product = product
        self.next = next
    def updateProduct(self, product):
        self.product = product
    def editProduct(self,u):
        self.product.name = u.name
        self.product.category = u.category
        self.product.description = u.description
        self.product.quantity = u.quantity
        self.product.productionCost = u.productionCost
        self.product.salePrice = u.salePrice
        self.product.date = u.date
        self.product.expiryDate = u.expiryDate
    
    def setLink(self, next):
        self.next = next
    def getProduct(self):
        return self.product
    def getNextNode(self):
        return self.next