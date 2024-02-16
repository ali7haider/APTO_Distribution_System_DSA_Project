
class product():
    def __init__(self,name,Id,category,quantity,description,productCost,salePrice,date,expiryDate):
        self.name = name
        self.Id = Id
        self.category = category
        self.description = description
        self.quantity = quantity
        self.productionCost = productCost
        self.salePrice = salePrice
        self.date = date
        self.expiryDate = expiryDate
    
    def name(self):
        return self.name
    def Id(self):
        return self.ID
    def category(self):
        return self.category
    def quantity(self):
        return self.quantity
    def description(self):
        return self.description
    def productionCost(self):
        return self.productionCost
    def salePrice(self):
        return self.salePrice
    def date(self):
        return self.date
    
    def setName(self,value):
        self.name = value
    def setId(self,value):
        self.Id = value
    def setCategory(self,value):
        self.category = value
    def setQuantity(self,value):
        self.quantity = value
    def setDescription(self,value):
        self.description = value
    def setProductionCost(self,value):
        self.productionCost = value
    def setSalePrice(self,value):
        self.salePrice = value
    def setDate(self,value):
        self.date = value