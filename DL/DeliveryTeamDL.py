# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 00:25:34 2022

@author: Digital Zone
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
import csv
from csv import writer
from BL.LinkedList import LinkedList
from BL.DeliveryMan import deliveryMan
from BL.file_paths import FilePaths
file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))

class deliveryManDL:
    deliveryManLinkedList = LinkedList()
    
    @staticmethod
    def loaddeliveryManInfo(path):
        with open(path , 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:      
              if row:                      
                Id = str(row[0])
                role = row[1]
                userName = str(row[2])
                name = str(row[3])
                password = str(row[4])
                cnic = str(row[5])
                email = str(row[6])
                cellNo = str(row[7])
                dateCreated = str(row[8])
                vehicle = str(row[9])
                salary = str(row[10])
                users = deliveryMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
                deliveryManDL.addDM(users)
        file.close()
    @staticmethod
    def addDM(s):
        # if salesManDL.salesMan.head is None: 
        deliveryManDL.deliveryManLinkedList.addToStart(s)
        # else:
        #     salesManDL.salesMan.addToEnd(s)
            
    @staticmethod   
    def addDMToFile(s):
        # print(s.password)
        lis=deliveryManDL().SaleAgentToLis(s)
        with open(file_paths.DeliveryManInfo,"a", newline='') as file:
            row=writer(file)
            row.writerow(lis)
            file.close()
    @staticmethod   
    def addAllDMToFile():
        # print(s.password)
        
        with open(file_paths.DeliveryManInfo,"w") as file:
            row=writer(file)
            start=deliveryManDL.deliveryManDL.head                          
            while start:
                s=start.getProduct()
                lis=deliveryManDL().SaleAgentToLis(s)
                row.writerow(lis)
                start=start.getNextNode()
            file.close()
    @staticmethod
    def SaleAgentToLis(salesAgent):
        
        # print(salesAgent.Id,d,salesAgent.login.userName,salesAgent.login.password,salesAgent.login.role,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
        return (str(salesAgent.Id),str(salesAgent.login.role),str(salesAgent.login.userName),str(salesAgent.name),str(salesAgent.login.password),str(salesAgent.cnic),str(salesAgent.email),str(salesAgent.cellNo),str(salesAgent.dateCreated),str(salesAgent.vehicle),str(salesAgent.salary))
    @staticmethod
    def EditDMData(previous,new):
        start=deliveryManDL.deliveryManDL.head 
        if start is None:
            print("Empty List")
        else:  
            while start:
                i=start.getProduct()
                if(previous.Id == i.Id and previous.login.role == i.login.role and previous.login.userName == i.login.userName and previous.cnic == i.cnic  and previous.cellNo == i.cellNo ):
                    i.Id=new.Id
                    i.login.role=new.login.role
                    i.login.userName=new.login.userName
                    i.name=new.name
                    i.login.password=new.login.password
                    i.cnic=new.cnic
                    i.email=new.email
                    i.cellNo=new.cellNo
                    i.dateCreated=new.dateCreated
                    i.vehicle=new.vehicle
                    i.salary=new.salary
                    print(i.Id , "Successfuly Updated")
                    break
                start=start.getNextNode()
        
        
    @staticmethod
    def allDMSalaries():
        tSum=0        
        start=deliveryManDL.deliveryManDL.head 
        if start is None:
            print("Empty List")
        else:                         
            while start:
                s=start.getProduct()
                if s.salary=="":
                    s.salary=0
                tSum=tSum+int(s.salary)
                start=start.getNextNode()
        return str(tSum)
        
            
        