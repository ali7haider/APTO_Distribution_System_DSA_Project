# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:16:46 2024

@author: Digital Zone
"""
import os
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from UI_Classes.saleTeamWindow_ui import Ui_MainWindow
from DL.ProductDL import productDL
from DL.OrderDL import orderDL

from BL.file_paths import FilePaths
from BL.User import user
from BL.Orders import order

from BL.Shopkeeper import shopkeeper
from datetime import date
from PyQt5.QtGui import QIntValidator
from datetime import datetime
from UI_Classes.viewStockWindow import ViewStockWindow
from PyQt5 import QtWidgets

class SaleTeamWindow(QMainWindow,Ui_MainWindow):
    
    order = None
    previousOrderId= ""
    previousQuantity = 0
    previousShopkeeperID = ""
    def __init__(self):
        super(SaleTeamWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
        self.btnSalesTeamViewStock.clicked.connect(self.viewStock)

        self.implementingValidation()
        self.addListsBehindComboBox()
        self.btnSalesTeamDashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.SalesTeamDashBoard))
        self.btnSalesTeamPlaceOrder.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.SalesAgentPlaceOrder))
        self.btnSalesTeamShopkeeper.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.SalesTeamShopkeeperpage))
        self.btnSalesTeamAccount.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.SalesTeamaccountDetails))
        self.cmbxProductID.activated.connect(self.changePrice)
        self.cmbxShopkeeperID.activated.connect(self.changeShopkeeperByID)
        # self.spnbxQuantity.valueChanged.connect(self.displayBill)
        self.btnSalesTeamAddToCart.clicked.connect(self.placeOrder)
        self.btnSalesTeamCompleteOrder.clicked.connect(self.completeOrder)
        self.btnSalesTeamClearText.clicked.connect(self.clearPlaceOrder)
        # self.txtbxOrderId.clicked.connect(lambda: OrderIdDisabler())
        # self.txtbxOrderId = ClickLineEdit(self)
        # self.connect(self.txtbxOrderId.SIGNAL("clicked()"),self.OrderIdDisabler())
        self.btnSalesTeamLogOut.clicked.connect(lambda: self.close())
    
    def viewStock(self):
        self.newq = ViewStockWindow()
        self.newq.show()
        # self.btnSalesTeamViewStock.clicked.connect(lambda: self.newq.populateAllStock())
        
    
    def addListsBehindComboBox(self):
        for item in shopkeeperDL.shopkeeperList:
            if item != None:
                self.cmbxShopkeeper.addItem(item.name)
                self.cmbxShopkeeperID.addItem(item.Id)
        for item in productDL.AllProducts:
            if item != None:
                self.cmbxProduct.addItem(item.name )
                self.cmbxProductID.addItem(item.Id )             
    # def displayBill(self):
    #     quantity = self.spnbxQuantity.value()
    #     price= self.spnbxPrice.value()
    #     totalBill = price*quantity
    #     self.txtbxDisplayBill.setText(str(totalBill))
    def changeShopkeeperByID(self):
        shopkeeperID = self.cmbxShopkeeperID.currentText()
        shop_Keeper = shopkeeperDL.searchShopkeeperById(shopkeeperID)
        self.cmbxShopkeeper.setCurrentText(shop_Keeper.name)
    def changePrice(self):
        productID= self.cmbxProductID.currentText()
        products = productDL.searchProductbyID(productID)
        # products.quantity = 0
        self.cmbxProduct.setCurrentText(products.name)
        self.spnbxPrice.setValue(products.salesPrice)
         
    def implementingValidation(self):
        self.txtbxOrderId.setInputMask("O_999999")
    def populateOrderTable(self,order):
        roww = 0
        self.tableSaleAgentOrders.setRowCount(len(order.productList))
        self.tableSaleAgentOrders.setColumnCount(5)
        self.tableSaleAgentOrders.setHorizontalHeaderLabels(['Delete','Product Name', 'Product ID','Sale Price','Quantity'])
        self.tableSaleAgentOrders.horizontalHeader().setVisible(True)
        self.tableSaleAgentOrders.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        print(len(order.productList))
        for i in range(len(productDL.productInCart)):
            row = productDL.productInCart[i]
            self.tableSaleAgentOrders.setItem(roww, 0 , QtWidgets.QTableWidgetItem('Delete'))
            self.tableSaleAgentOrders.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.name)))
            self.tableSaleAgentOrders.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.ID)))
            self.tableSaleAgentOrders.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.salesPrice))))
            self.tableSaleAgentOrders.setItem(roww, 4 , QtWidgets.QTableWidgetItem((str(row.quantity ))))
            roww = roww + 1
    # def orderIDSync(self):
    #     if len(productDL.productInCart)!=0:
    #         self.txtbxOrderId.setReadOnly(True)
    #         self.cmbxShopkeeper.setEnabled(True)
    
    def placeOrder(self):
        orderID, price ,quantity = 0,0,0
        print(len(productDL.productInCart))
        if len(productDL.productInCart) >-1 :
            self.txtbxOrderId.setReadOnly(True)
            print("txt disabled")
            self.cmbxShopkeeper.setEnabled(False)
            self.cmbxShopkeeperID.setEnabled(False)
        orderID=self.txtbxOrderId.text()
        saleAgent = user.UserLoggedIn
        shopkeeperName = self.cmbxShopkeeper.currentText()
        shopkeeperID = self.cmbxShopkeeperID.currentText()
        singleShopkeeper = shopkeeperDL.searchShopkeeper(shopkeeperName,shopkeeperID)
        productName = self.cmbxProduct.currentText()
        productID= self.cmbxProductID.currentText()
        products = productDL.searchProduct(productName, productID)
        today = date.today()
        orderDate=  today.strftime("20%y-%m-%d")
        deliveryDate = self.dateDeliveryDate.date().toPyDate()
        print(deliveryDate)
        quantity = self.spnbxQuantity.value()
        price= self.spnbxPrice.value()
        # productDL.productQuantityDecreaser(productID, quantity)
        totalBill = productDL.CartRepair(productID, quantity)
        self.txtbxDisplayBill.setText(str(totalBill))
        
        singleOrder = order(str(orderID), singleShopkeeper, saleAgent,
                            productDL.productInCart,totalBill, "New", None,
                            orderDate,deliveryDate,"Not Paid","4444",quantity)
        
        
        if orderID != 'O_' and price > 0 and quantity > 0 :
            self.lblOrderIDError.setText("")
            self.lblPriceError.setText("")
            self.lblQuantityError.setText("")
            self.populateOrderTable(singleOrder)
            self.cmbxProduct.setCurrentIndex(0)
            self.cmbxProductID.setCurrentIndex(0)
            today = date.today()
            orderDate=  today.strftime("20%y-%m-%d")
            self.spnbxQuantity.setValue(0)
            self.spnbxPrice.setValue(0)
        else:           
            if orderID == 'O_':
                self.lblOrderIDError.setText("This field is required.")
            if price == 0:
                self.lblPriceError.setText("This field is required.Select Product ID!")
            if quantity == 0:
                self.lblQuantityError.setText("This field is required.")
            else:
                self.lblOrderIDError.setText("")
                self.lblPriceError.setText("")
                self.lblQuantityError.setText("")
        return singleOrder
            
    def completeOrder(self):
        if(self.order != None):
            orderDL.ordersList.append(self.order)
        self.printList()
        self.clearPlaceOrder()
        print(len(productDL.productInCart))
    def printList(self): 
        for i in orderDL.ordersList:
            for j in i.productList :
                print(i.orderID, i.shopkeeper.name , i.saleAgent.userName ,j.name , j.ID, j.quantity )
                
    def clearPlaceOrder(self):
         self.txtbxOrderId.setReadOnly(False)
         self.cmbxShopkeeper.setEnabled(True)
         self.cmbxShopkeeperID.setEnabled(True)
         self.txtbxOrderId.setText("")
         self.cmbxShopkeeper.setCurrentIndex(0)
         self.cmbxShopkeeperID.setCurrentIndex(0)
         self.cmbxProduct.setCurrentIndex(0)
         self.cmbxProductID.setCurrentIndex(0)
         today = date.today()
         orderDate=  today.strftime("20%y-%m-%d")
         self.spnbxQuantity.setValue(0)
         self.spnbxPrice.setValue(0)
         self.tableSaleAgentOrders.setRowCount(0)
         productDL.productInCart.clear()