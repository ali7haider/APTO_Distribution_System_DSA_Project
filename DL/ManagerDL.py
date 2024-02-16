import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.Manager import manager
import os
from csv import writer
from BL.LinkedList import LinkedList
import csv
class managerDL:
    managers = LinkedList()
    managerCount=0
    
    @staticmethod
    def loadManagerInfo(path):
        with open(path , 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:
              if row: 
                Id = str(row[0])
                role = row[1]
                userName = row[2]
                name = row[3]
                password = row[4]
                cnic = row[5]
                email = row[6]
                cellNo = row[7]
                dateCreated = row[8]
                salary=row[9]
                users = manager(userName, password,role, name, cnic, email, cellNo, Id, dateCreated,salary)
                managerDL.addManager(users)
        file.close()
    @staticmethod
    def addManager(s):
        # if salesManDL.salesMan.head is None: 
        managerDL.managers.addToStart(s)
        managerDL.managerCount = managerDL.managerCount + 1
    
    
    @staticmethod   
    def addManagerToFile(p,s):
        # print(s.password)
        lis=managerDL().SaleAgentToLis(s)
        with open(p,"a", newline='') as file:
            row=writer(file)
            row.writerow(lis)
            file.close()
    @staticmethod
    def SaleAgentToLis(salesAgent):
        
        # print(salesAgent.Id,d,salesAgent.login.userName,salesAgent.login.password,salesAgent.login.role,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
        return (str(salesAgent.Id),str(salesAgent.login.role),str(salesAgent.login.userName),str(salesAgent.name),str(salesAgent.login.password),str(salesAgent.cnic),str(salesAgent.email),str(salesAgent.cellNo),str(salesAgent.dateCreated),str(salesAgent.salary))
    @staticmethod   
    def addAllManagerToFile(path):
        # print(s.password)
        
        with open(path,"w") as file:
            row=writer(file)
            start=managerDL.managers.head                          
            while start:
                s=start.getProduct()
                lis=managerDL().SaleAgentToLis(s)
                row.writerow(lis)
                start=start.getNextNode()
            file.close()
            
    @staticmethod
    def deleteManager(d):
        managerDL.managers.remove(d)
        managerDL.managerCount = managerDL.managerCount - 1
    @staticmethod
    def EditManager(previous,new):
        start=managerDL.managers.head 
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
    def allManagerSalaries():
        tSum=0        
        start=managerDL.managers.head 
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
