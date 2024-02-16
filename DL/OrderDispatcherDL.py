# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:52:38 2022

@author: Digital Zone
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from BL.OrderDispatcher import orderDispatcher
import os
import pandas as pd
import csv
from csv import writer
from BL.Credentials import credential
from BL.LinkedList import LinkedList
from BL.User import user
class orderDispatcherDL:
    orderDispatcherLinkedList = LinkedList()
    oderDispactherCount=0
    
    @staticmethod
    def loadODInfo(path):
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
                salary = str(row[9])
                users = orderDispatcher(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,salary)
                orderDispatcherDL.addODMan(users)
        file.close()
    @staticmethod
    def deleteOrderDispatcher(d):
        orderDispatcherDL.orderDispatcherLinkedList.remove(d)
        orderDispatcherDL.oderDispactherCount = orderDispatcherDL.oderDispactherCount - 1
    
    @staticmethod
    def addODMan(s):
        # if salesManDL.salesMan.head is None: 
        orderDispatcherDL.orderDispatcherLinkedList.addToStart(s)
        orderDispatcherDL.oderDispactherCount = orderDispatcherDL.oderDispactherCount + 1
        # else:
        #     salesManDL.salesMan.addToEnd(s)  
    @staticmethod   
    def addODToFile(path,s):
        # print(s.password)
        lis=orderDispatcherDL().SaleAgentToLis(s)
        with open(path,"a", newline='') as file:
            row=writer(file)
            row.writerow(lis)
            file.close()
    @staticmethod   
    def addAllODToFile(path):
        # print(s.password)
        
        with open(path,"w") as file:
            row=writer(file)
            start=orderDispatcherDL.orderDispatcherLinkedList.head                          
            while start:
                s=start.getProduct()
                lis=orderDispatcherDL.SaleAgentToLis(s)
                row.writerow(lis)
                start=start.getNextNode()
            file.close()
    @staticmethod
    def SaleAgentToLis(salesAgent):
        
        # print(salesAgent.Id,d,salesAgent.login.userName,salesAgent.login.password,salesAgent.login.role,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
        return (str(salesAgent.Id),str(salesAgent.login.role),str(salesAgent.login.userName),str(salesAgent.name),str(salesAgent.login.password),str(salesAgent.cnic),str(salesAgent.email),str(salesAgent.cellNo),str(salesAgent.dateCreated),str(salesAgent.salary))
    @staticmethod
    def EditODDataToList(previous,new):
        start=orderDispatcherDL.orderDispatcherLinkedList.head 
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
                    i.salary=new.salary
                    print(i.Id , "Successfuly Updated")
                    break
                start=start.getNextNode()
    @staticmethod
    def allODSalaries():
        tSum=0        
        start=orderDispatcherDL.orderDispatcherLinkedList.head 
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
        