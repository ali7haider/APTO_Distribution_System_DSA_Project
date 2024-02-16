import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.Shopkeeper import shopkeeper
import os

class shopkeeperDL:
    shopkeeperList = []
    s1 = shopkeeper('dssad', 1232, 'Ali', 32131232313, 'ds@ds', '03232233232', 'S01', '2022-02-12', 'address', 1233123)
    s2 = shopkeeper('dssad', 1232, 'Fahad', 32131232313, 'ds@ds', '03232233232', 'S02', '2022-02-12', 'address', 1233123)
    shopkeeperList.append(s1)
    shopkeeperList.append(s2)
    
    @staticmethod
    def searchShopkeeperById(Id):
        for i in shopkeeperDL.shopkeeperList:
            if i.Id == Id:
                return i
    
    @staticmethod
    def searchShopkeeper(shopkeeperName, Id):
        for i in shopkeeperDL.shopkeeperList:
            if i.name == shopkeeperName and i.Id == Id:
                return i

        
    # @staticmethod
    # def loadAdminInfo(path):
    #     with open(path , 'r') as file:
    #       csvreader = csv.reader(file)
    #       for row in csvreader:
    #         Id = row[0]
    #         role = row[1]
    #         userName = row[2]
    #         name = row[3]
    #         password = row[4]
    #         cnic = row[5]
    #         email = row[6]
    #         cellNo = row[7]
    #         dateCreated = row[8]
    #         users = admin(userName, password, name, cnic, email, cellNo, Id, dateCreated)
    #         adminDL.owner.append(users)
    #         print(users.Id)
    #         print
    #     file.close()
    # @staticmethod
    # def searchAdmin(login):
    #     for i in adminDL.owner:
    #         print(login.userName ," ", i.login.userName," " ,login.password," " ,i.login.password)
    #         if(login.userName == i.login.userName and login.password == i.login.password):
    #             return True
    #     return False
    # @staticmethod
    # def deleteAdmin(login):
    #     for i in adminDL.owner:
    #         print(login.userName ," ", i.login.userName," " ,login.password," " ,i.login.password)
    #         if(login.userName == i.login.userName and login.password == i.login.password):
    #             adminDL.owner.remove(i)
    #     return False
            
            
            