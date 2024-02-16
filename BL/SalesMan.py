import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.Credentials import credential
from BL.User import user
class salesMan(user):
    def __init__(self,userName,password,role,name,cnic,email,cellNo,Id,dateCreated,vehicle,salary):
        self.login = credential(userName, password, role)
        self.totalorder = 0
        self.salary = salary
        self.vehicle = vehicle
        super(). __init__(name,cnic,email,cellNo,Id , dateCreated)
    def totalOrder(self):
        return self.totalOrder   
    def salary(self):
        return self.salary    
    def vehicle(self):
        return self.vehicle

    def setTotalOrder(self,value):
        self.totalOrder = value
    def setSalary(self,value):
        self.salary = value
    def setVehicle(self,value):
        self.vehicle = value