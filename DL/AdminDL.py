import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from BL.Admin import admin
import csv
class adminDL:
    owner = []
    
    @staticmethod
    def loadAdminInfo(path):
        with open(path , 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:
              if row:
                Id = row[0]
                role = row[1]
                userName = row[2]
                name = row[3]
                password = row[4]
                cnic = row[5]
                email = row[6]
                cellNo = row[7]
                dateCreated = row[8]
                users = admin(userName, password, name, cnic, email, cellNo, Id, dateCreated)
                adminDL.owner.append(users)
        file.close()
    @staticmethod
    def searchAdmin(login):
        for i in adminDL.owner:
            print(login.userName ," ", i.login.userName," " ,login.password," " ,i.login.password)
            if(login.userName == i.login.userName and login.password == i.login.password):
                return True
        return False
    @staticmethod
    def deleteAdmin(login):
        for i in adminDL.owner:
            print(login.userName ," ", i.login.userName," " ,login.password," " ,i.login.password)
            if(login.userName == i.login.userName and login.password == i.login.password):
                adminDL.owner.remove(i)
        return False
            
            
            