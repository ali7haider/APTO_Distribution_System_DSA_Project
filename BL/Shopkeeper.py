from User import user

class shopkeeper(user):
    def __init__(self,userName,password,name,cnic,email,cellNo,Id,dateCreated
                 ,address,totalPendingBills):
        self.address = address
        self.totalPendingBills= totalPendingBills
        self.orderList = []
        
        super(). __init__(name,cnic,email,cellNo,Id , dateCreated)
    def OrderList(self):
        return self.orderList
    
    # def addOrdertoList(self,Order)