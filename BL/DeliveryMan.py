# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 00:25:13 2022

@author: Digital Zone
"""

from BL.Credentials import credential
from BL.User import user
class deliveryMan(user):
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