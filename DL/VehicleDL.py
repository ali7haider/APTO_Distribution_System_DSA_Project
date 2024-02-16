# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:26:52 2022

@author: Digital Zone
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
import csv
from csv import writer
from BL.LinkedList import LinkedList
from BL.Vehicle import vehicle
class vehicleDL:
    vehicleLinkedList = LinkedList()
    vehicleCount = 0
    @staticmethod
    def loadVehicleInfo(path):
        with open(path , 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:      
              if row:                      
                Id = str(row[0])
                name = row[1]
                brand = str(row[2])
                category = str(row[3])
                capacity = str(row[4])
                number = str(row[5])
                price = str(row[6])
                dateCreated = row[7]
                v = vehicle(Id,name,brand,category ,capacity, number,price, dateCreated)
                vehicleDL().addVehicle(v)
        file.close()
    @staticmethod
    def addVehicle(s):
        # if vehicleDL().vehicleLinkedList.head is None: 
        vehicleDL().vehicleLinkedList.addToStart(s)
        vehicleDL.vehicleCount = vehicleDL.vehicleCount + 1
        # else:
        #     vehicleDL.vehicleLinkedList.addToEnd(s)  
    @staticmethod
    def deleteVehicle(v):
        vehicleDL.vehicleLinkedList.remove(v)
        vehicleDL.vehicleCount = vehicleDL.vehicleCount - 1
    @staticmethod   
    def addVehicleToFile(path,s):
        # print(s.password)
        lis=vehicleDL().vehicleToLis(s)
        with open(path,"a", newline='') as file:
            row=writer(file)
            row.writerow(lis)
            file.close()
    @staticmethod   
    def addAllVehicleToFile(path):
        # print(s.password)
        
        with open(path,"w") as file:
            row=writer(file)
            start=vehicleDL.vehicleLinkedList.head                          
            while start:
                s=start.getProduct()
                lis=vehicleDL().vehicleToLis(s)
                row.writerow(lis)
                start=start.getNextNode()
            file.close()
    @staticmethod
    def vehicleToLis(s):
        
        # print(salesAgent.Id,d,salesAgent.login.userName,salesAgent.login.password,salesAgent.login.role,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
        return (str(s.Id),str(s.name),str(s.brand),str(s.category),str(s.capacity),str(s.number),str(s.price),s.dateCreated)
    @staticmethod
    def EditVehicle(previous,new):
        start=vehicleDL.vehicleLinkedList.head  
        if start is None:
            print("Empty List")
        else:  
            while start:
                i=start.getProduct()
                if(previous.Id == i.Id and previous.number == i.number):
                    i.Id=new.Id
                    i.name=new.name
                    i.brand=new.brand
                    i.category=new.category
                    i.capacity=new.capacity
                    i.number=new.number
                    i.price=new.price
                    i.dateCreated=new.dateCreated
                    print(i.Id , "Successfuly Updated")
                    break
                start=start.getNextNode()
    @staticmethod
    def allVehicle():
        tSum=0        
        start=vehicleDL.vehicleLinkedList.head  
        if start is None:
            print("Empty List")
        else:                         
            while start:
                tSum=tSum+1
                start=start.getNextNode()
        return str(tSum)