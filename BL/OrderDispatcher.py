# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:48:43 2022

@author: Digital Zone
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.Credentials import credential
from BL.User import user
class orderDispatcher(user):
    def __init__(self,userName,password,role,name,cnic,email,cellNo,Id,dateCreated,salary):
        self.login = credential(userName, password, role)
        self.totalorder = 0
        self.totalOrderDispatched=0
        self.salary = salary
        super(). __init__(name,cnic,email,cellNo,Id , dateCreated)
    def totalOrderDispatched(self):
        return self.totalOrderDispatched   
    def salary(self):
        return self.salary    

    def setTotalOrderDispatched(self,value):
        self.totalOrderDispatched = value
    def setSalary(self,value):
        self.salary = value
    def setVehicle(self,value):
        self.vehicle = value