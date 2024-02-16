# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:26:40 2022

@author: Digital Zone
"""

from BL.Credentials import credential
from BL.User import user
class vehicle():
    def __init__(self,Id,name,brand,category,capacity,number,price,dateCreated):
        self.Id=Id
        self.name = name
        self.brand = brand
        self.category = category
        self.capacity=capacity
        self.number=number
        self.price=price
        self.dateCreated=dateCreated
    def Id(self):
        return self.Id   
    def name(self):
        return self.name    
    def brand(self):
        return self.brand
    def category(self):
        return self.category
    def capacity(self):
        return self.capacity
    def number(self):
        return self.number
    def price(self):
        return self.price
    def dateCreated(self):
        return self.dateCreated

    def setId(self,value):
        self.Id = value
    def setName(self,value):
        self.name = value
    def setBrand(self,value):
        self.brand = value
    def setCategory(self,value):
        self.category = value
    def setCapacity(self,value):
        self.capacity = value
    def setNumber(self,value):
        self.number = value
    def setPrice(self,value):
        self.price = value
    def setDateCreatde(self, value):
        self.dateCreated=value
    