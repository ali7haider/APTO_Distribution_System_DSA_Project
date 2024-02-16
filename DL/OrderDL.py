import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.Orders import order
from BL.Product import product
import os
import pandas as pd
import csv
class orderDL:
    ordersList = []
    
    @staticmethod
    def addOrderToList(order):
        orderDL.ordersList.append(order)
    @staticmethod
    def deleteOrder(order):
        orderDL.ordersList.append(order)
    @staticmethod
    def writeOrderData(path):
        for order in orderDL.ordersList:
            f = open(path, 'w')
            writer = csv.writer(f)
            row= [str(order.orderID),str(order.shopkeeper),str(order.saleAgent),str(order.productList),
                  str(order.client),str(order.totalBill),str(order.status),
                  str(order.deliveryBoy),str(order.orderDate),str(order.deliveryDate),str(order.billStatus),
                  str(order.pendingBill)]
            writer.writerow(row)
            f.close()
            
# orderID,shopkeeper,saleAgent,productList,totalBill,status
#              ,deliveryBoy,orderDate,deliveryDate,billStatus,pendingBill,quantity)            
            
    @staticmethod
    def uniqueOrderId(self,Id):
        for i in orderDL.ordersList:
            if i in orderDL.ordersList == Id :
                return True
        return False
    @staticmethod
    def loadOrderData(path):
        with open(path , 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:
            orderID     = row[0]
            shopkeeper  = row[1]
            saleAgent   = row[2]
            productList = row[3]
           
            orderPlacer = row[5]
            quantity    = row[6] 
            totalBill =   row[6]
            status =      row[7]
            deliveryBoy = row[8]
            orderDate =   row[9]
            deliveryDate= row[10]
            billStatus =  row[11]
            pendingBill = row[12]
           
            singleOrder = order(orderID,shopkeeper,saleAgent,productList,
                                client,orderPlacer,totalBill,status,
                                deliveryBoy,orderDate,deliveryDate,billStatus,
                                pendingBill)
            
            orderDL.ordersList.append(singleOrder)
            # print(users.Id)
            print
        file.close()
        
    # @staticmethod
    # def searchOrder(order):
    #     for i in orderDL.ordersList:
    #         print(order.orderID ," ", order.shopkeeper ," ", order.saleAgent 
    #               ," ", order.productList ," ", order.client )
    #         if(order.orderID == i.orderID and order.shopkeeper == i.shopkeeper
    #            and order.saleAgent = i.saleAgent and order.productList == i.productList
    #            and ):
    #             return True
    #     return False
    
    
    