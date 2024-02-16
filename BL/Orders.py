from BL.Product import product
# from User import user
class order():
    def __init__(self,orderID,shopkeeper,saleAgent,productList,totalBill,status
                 ,deliveryBoy,orderDate,deliveryDate,billStatus,pendingBill,quantity):
        self.orderID = str(orderID)
        self.shopkeeper = shopkeeper
        self.saleAgent = saleAgent
        self.productList = productList
        self.totalBill = totalBill
        self.deliveryDate = deliveryDate
        self.quantity = quantity
        self.status = status
        self.deliveryBoy = deliveryBoy
        self.orderDate = orderDate
        self.billStatus = billStatus
        self.pendingBill = pendingBill
        
        
        
        # Getter Funcs
        def orderID(self):
            return self.orderID
        def shopkeeper(self):
            return self.shopkeeper
        def saleAgent(self):
            return self.saleAgent
        def productList(self):
            return self.productList
        def totalBill(self):
            return self.totalBill
        def status(self):
            return self.status
        def deliveryBoy(self):
            return self.deliveryBoy
        def orderDate(self):
            return self.orderDate
        def deliveryDate(self):
            return self.deliveryDate
        def billStatus(self):
            return self.billStatus
        def pendingBill(self):
            return self.pendingBill
        
        # setter Funcs
        def setOrderID(self,value):
            self.orderID = value
        def setShopkeeper(self,value):
            self.shopkeeper = value
        def setSaleAgent(self,value):
            self.saleAgent = value
        def addProductToProductList(self,value):
            self.productList.append(value)
        def setClient(self,value):
            self.client = value
        def setTotalBill(self,value):
            self.totalBill = value
        def setStatus(self,value):
            self.status = value
        def setDeliveryBoy(self,value):
            self.deliveryBoy = value
        def setOrderDate(self,value):
            self.orderDate = value
        def setDeliveryDate(self,value):
            self.deliveryDate = value
        def setBillStatus(self,value):
            self.billStatus = value
        def setPendingBill(self,value):
            self.pendingBill = value
        