# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 23:57:47 2022

@author: Digital Zone
"""

from BL.Credentials import credential
from BL.User import user
class manager(user):
    def __init__(self,userName,password,role,name,cnic,email,cellNo,Id,dateCreated,salary):
        self.salary = salary
        self.login = credential(userName, password, "Manager")
        super(). __init__(name,cnic,email,cellNo,Id , dateCreated)