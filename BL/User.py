from datetime import datetime
class user:
    UserLoggedIn = None
    def __init__(self,name,cnic,email,cellNo,Id , dateCreated):
        self.name = name
        self.cnic = cnic
        self.email = email
        self.cellNo = cellNo
        self.dateCreated = dateCreated
        self.Id = Id
    
    # def userLoggedIn(self):
    #     return self.UserLoggedIn
    def name(self):
        return self.name
    def cnic(self):
        return self.cnic
    def email(self):
        return self.email
    def cellNo(self):
        return self.cellNo
    def dateCreated(self):
        return self.dateCreated
    def Id(self):
        return self.Id
    
    # def setUserLoggedIn(self,value):
    #     self.UserLoggedIn = value
    def setName(self,value):
        self.name = value
    def setCnic(self,value):
        self.cnic = value
    def setEmail(self,value):
        self.email = value
    def setCellNo(self,value):
        self.cellNo = value
    def setDateCreatde(self,value):
        self.dateCreated = value
    