import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.Product import product
import os
import pandas as pd
import csv
import copy
from BL.Orders import order
from csv import writer
from BL.LinkedList import LinkedList
class productDL:
    AllProducts = []
    P1 = product('Nestle', 'P_01', 'category', 122, 'description', 100, 100, '2022-12-16',"2022-12-18")
    P2 = product('Pepsi', 'P_02', 'category', 4324, 'description', 200, 200, '2022-12-16',"2022-12-18")
    AllProducts.append(P1)
    AllProducts.append(P2)
    productInCart = []
    productList = LinkedList()
    productCount = 0
    @staticmethod
    def addProductToList(product):
        # if(productDL.productList.head == None):
        productDL.productList.addToStart(product)
        # else:
        #     productDL.productList.addToEnd(product)
        productDL.productCount = productDL.productCount + 1
    @staticmethod
    def deleteProduct(product):
        productDL.productList.remove(product)
        productDL.productCount = productDL.productCount - 1
    @staticmethod
    def storeProductInFile(path , p):
        lis = productDL().objectLis(p)
        with open(path, 'a',newline='') as file:
            row=csv.writer(file)
            row.writerow(lis)
            file.close()
        
    @staticmethod
    def objectLis(p):
        return (str(p.Id),str(p.name),str(p.category),str(p.description),str(p.quantity),str(p.productionCost),str(p.date),str(p.expiryDate),str(p.salePrice))
    @staticmethod
    def editProduct(p,edited):
        start = productDL().productList.head
        if start is None:
            return False

        while start:
            if(start.getProduct().Id == p.Id):
                start.editProduct(edited)
                break
            start = start.next

    @staticmethod
    def storeAllProductInFile(path):
        f = open(path, 'w' ,newline='')
        writer = csv.writer(f)
        start = productDL().productList.head
        if start is None:
            return False
        while start:
            p = start.getProduct()
            row= [str(p.Id),str(p.name),str(p.category),str(p.description),str(p.quantity),
                  str(p.productionCost),str(p.date),str(p.expiryDate),str(p.salePrice)]
            writer.writerow(row)
            start = start.getNextNode()
        f.close()            
    @staticmethod
    def loadProductsFromFile(path):
        with open(path , 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:
            Id =     row[0]
            name =  row[1]
            category =   row[2]
            description = row[3]
            quantity = int(row[4])
            productionCost = int(row[5])
            date =  row[6]
            expiryDate = row[7]
            salePrice =   row[8]
            p = product(name, Id, category, quantity, description, productionCost, salePrice, date, expiryDate)
            productDL.addProductToList(p)
        file.close()
    
    
    
    @staticmethod
    def CartRepair(productID,quantity):
        product = productDL.productQuantityDecreaser(productID, quantity)
        flag = False
        print("Product Quantity 1:",product.quantity)
        product.quantity = quantity
        print("Product Quantity 2:",product.quantity)
        # print("order quantity",quantity,"\n")
        for i in productDL.productInCart:
            if i.ID == productID:
                cartquantity = i.quantity
                print(cartquantity)
                i.quantity = i.quantity + quantity
                flag = True
        if(flag == False):
            productDL.productInCart.append(product)
        bill,quantity,price=0,0,0
        for i in productDL.productInCart:
            quantity = i.quantity
            price = i.salesPrice
            bill = bill + (price*quantity)
        print("Product Quantity 3:",product.quantity)
        # product.quantity = product.quantity - quantity
        # print("Product Quantity 1:",product.quantity)
        return bill
    
    def productQuantityDecreaser(productID,quantity):
        # product = productDL.searchProductbyID(productID)
        for i in productDL.AllProducts:
            if i.ID == productID:
                i.quantity = i.quantity - quantity
                print("Product Quantity 0:",product.quantity)
                return copy.copy(i)
        # print("Product Quantity 1232:",product.quantity)
    
    @staticmethod
    def searchProductbyID(productID):
        for i in productDL.AllProducts:
            if  i.ID == productID:
                # i.quantity = i.quantity - quantity
                return copy.copy(i)
    @staticmethod
    def searchProduct(productName, productID):
        for i in productDL.AllProducts:
            if i.name == productName and i.ID == productID:
                # i.quantity = i.quantity - quantity
                return i
        # return "Product Not Found!"
    @staticmethod
    def addOrderToList(order):
        productDL.productList.append(order)
    @staticmethod
    def deleteOrder(order):
        productDL.productList.remove(order)
    @staticmethod
    def writeOrderData(path):
        for order in productDL.productList:
            f = open(path, 'w')
            writer = csv.writer(f)
            row= [str(order.orderID),str(order.shopkeeper),str(order.saleAgent),str(order.productList),
                  str(order.client),str(order.orderPlacer),str(order.totalBill),str(order.status),
                  str(order.deliveryBoy),str(order.orderDate),str(order.deliveryDate),str(order.billStatus),
                  str(order.pendingBill)]
            writer.writerow(row)
            f.close()
        
    @staticmethod
    def loadOrderData(path):
        with open(path , 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:
            orderID =     row[0]
            shopkeeper =  row[1]
            saleAgent =   row[2]
            productList = row[3]
            client =      row[4]
            orderPlacer = row[5]
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
            
            productDL.productList.append(singleOrder)
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
    
    
    