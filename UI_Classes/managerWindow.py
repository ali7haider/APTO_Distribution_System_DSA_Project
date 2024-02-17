# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:11:19 2024

@author: Digital Zone
"""

import os
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from UI_Classes.managerWindow_ui import Ui_MainWindow
from DL.OrderDispatcherDL import orderDispatcherDL
from DL.DeliveryManDL import deliveryManDL
from DL.VehicleDL import vehicleDL
from DL.SalesManDL import salesManDL
from DL.ManagerDL import managerDL
from DL.CategoryDL import categoryDL
from DL.ProductDL import productDL
from BL.file_paths import FilePaths
from BL.Product import product
from BL.Vehicle import vehicle
from BL.OrderDispatcher import orderDispatcher
from BL.DeliveryMan import deliveryMan
from BL.SalesMan import salesMan
from BL.Manager import manager
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from datetime import date
import shutil
from datetime import timedelta
from UI_Classes.addSaleAgentWindow import AddSaleAgentWindow

class ManagerWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(ManagerWindow, self).__init__()
        # Set up the user interface from the generated class
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))       

        
        
        #Widget Changer
        self.stackedWidget.setCurrentWidget(self.managerDashboard)
        self.btnManagerDashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.managerDashboard))
        self.btnManagerAgentManagement.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.agentManagement))
        self.btnManagerOrderDispatcher.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.orderDispatcher))
        self.btnManagerDeliveryManagement.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.DeliveryManagement))
        self.btnManagerPaymentCollection.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.paymentCollection))
        self.btnManagerOrderManagement.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.orderManagement))
        self.btnManagerInventoryManagement.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.inventoryManagement))
        self.btnManagerVehicle.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.vehiclesManagement))
        self.btnManagerReports.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.reports))
        self.btnManagerAccount.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Account))
        self.btnManagerLogOut.clicked.connect(lambda: self.close())
        self.loadProductGraph()
        self.btnManagerDashboard.clicked.connect(lambda:self.loadProductGraph())
        self.btnManagerReports.clicked.connect(lambda: self.loadReports())
        self.btnManagerDashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.loadSalesInLast7Day()))
        self.loadSalesInLast7Day()
        
        
        self.btnManagerGenerateReports.clicked.connect(lambda: self.generateReportPage())

       


        
        #Sale Agent CRUD
        self.btnManagerAgentManagement.clicked.connect(self.loadSaleAgentData)
        self.btnAddNewAgent.clicked.connect(lambda: self.addNewAgent())
        self.btnManagerEditAgent.clicked.connect(lambda: self.editDataSaleAgent())
        self.btnManagerAgentDelete.clicked.connect(lambda: self.deleteSaleAgent())
        self.btnManagerAgentCSV.clicked.connect(lambda: self.exportSaleAgentData())
        self.loadingSaleAgentLabels()  
        
        #Delivery Man CRUD
        self.btnManagerDeliveryManagement.clicked.connect(self.loadDMData)
        self.btnAddNewDeliveryMen.clicked.connect(lambda: self.addNewDM())
        self.btnManagerEditDeliveryMen.clicked.connect(lambda: self.editDM())
        self.btnManagerDeliveryMenDelete.clicked.connect(lambda: self.deleteDM()) 
        self.btnManagerDeliveryMenCSV.clicked.connect(lambda: self.exportDeliveryMan())
        self.loadingDMLabels()
        
        #Order Dispacther CRUD
        self.loadOrderDispatcherData()
        self.btnAddNewOrderDispatcher.clicked.connect(lambda: self.addNewOrderDispatcher())
        self.btnManagerEditOrderDispatcher.clicked.connect(lambda: self.editOD())
        self.btnManagerOrderDispatcherDelete.clicked.connect(lambda: self.deleteOD())  
        self.btnManagerOrderDispatcherCSV.clicked.connect(lambda: self.exportOrderDispatcher())
        self.loadingODLabels()
        
        #Vehicle CRUD
        self.loadVehicleData()
        self.btnManagerAddNewVehicle.clicked.connect(lambda: self.addVehicle())
        self.btnManagerEditVehicle.clicked.connect(lambda: self.EditVehicle())
        self.btnManagerDeleteVehicle.clicked.connect(lambda: self.deleteVehicle())  
        self.loadingVehicleLabels()
        
        #Product CRUD
        self.btnManagerInventoryManagement.clicked.connect(lambda: self.loadTableProduct())
        self.btnManagerAddProduct.clicked.connect(lambda: self.loadTableProduct())
        self.btnManagerAddProduct.clicked.connect(lambda: self.addProduct())
        self.btnManagerDeleteProduct.clicked.connect(lambda: self.deleteProduct())
        self.btnManagerEditProduct.clicked.connect(lambda: self.editProduct())
        self.btnManagerProductCSV.clicked.connect(lambda: self.exportProductCSV())
        self.loadTableProduct()

        #Manager Account
        self.btnManagerAccount.clicked.connect(lambda: self.accountDetails())
        self.changeUserNameOrPassword.clicked.connect(lambda: self.changeUserNameAndPassword())

    def generateReportPage(self):
         pass
         # self.geneReport=GenerateReport()
         # self.geneReport.show()    

    def loadReports(self):
        employees=["Sales Agent","Order Dispatcher","Delivery Man"]
        num=[]
        num.append(salesManDL().saleAgentCount)
        num.append(orderDispatcherDL().oderDispactherCount)
        num.append(deliveryManDL().deliveryManCount)
        colors = ['#4E9C81','#49DCB1','#00917C']
        plt.figure(figsize=(8,6))
        explode = (0, 0.1, 0)       
        fig1, ax1 = plt.subplots()
        ax1.pie(num, explode=explode, labels=employees,colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')        
        plt.savefig("allEmployeesManagerGraph.png", transparent=True)
        plt.show()
        # pixmap=QPixmap("save_figure.png")
        # item = QGraphicsPixmapItem(pixmap)
        # scene.addItem(item)
        pixmap = QPixmap('allEmployeesManagerGraph.png')
        self.lblManagerSaleInLast7Days.setPixmap(pixmap)
        


    def loadSalesInLast7Day(self):
        df=pd.read_csv(self.file_paths.SalesPerDate,header=None,usecols=[0,1],infer_datetime_format=True)
        sales=df[0].values.tolist()
        dates=df[1].values.tolist()
        sa=[]
        da=[]
        dateToday= date.today()
        today = date.today()
        for i in range(7):
            yesterday =(today - timedelta(days = i+1)).strftime("%d/%m/%Y")
            tSum=0
            for j in range(len(dates)):
                if dates[j]==str(yesterday):
                    tSum=tSum+int(sales[j])
            
            sa.append(tSum) 
            da.append(yesterday)
        max_val = max(sa)
        idx = sa.index(max_val)
        best=str(da[idx])
        df = pd.Timestamp(best)
        bestSale=max(sa)
        bestDay=df.day_name()
        
        min_val = min(sa)
        idx = sa.index(min_val)
        worst=str(da[idx])
        df = pd.Timestamp(worst)
        worstSale=min(sa)
        worstDay=df.day_name()
        self.lblBestSellingDay.setText(str(bestDay))
        self.lblBestSellingNo.setText(str(bestSale))
        self.lblWorstSellingDay.setText(str(worstDay))
        self.lblWorstSellingNo.setText(str(worstSale))
        plt.figure(figsize=(20,4))
        plt.xlabel("Date",fontsize=14)
        plt.ylabel("Sales",fontsize=14)
        plt.bar(da,sa,color='#48ACAC')
        plt.savefig("salesLast7Days.png", transparent=True)
        # pixmap=QPixmap("save_figure.png")
        # item = QGraphicsPixmapItem(pixmap)
        # scene.addItem(item)
        pixmap = QPixmap('salesLast7Days.png')        
        self.lblLast12MonthRevenue.setPixmap(pixmap)
        self.lblManagerRenevueInLast12Months.setPixmap(pixmap)
    def loadProductGraph(self):
        df = pd.read_csv(self.file_paths.ProductsInfo,header = None, usecols=[2,4])
        category=df[2].values.tolist()
        quantity=df[4].values.tolist()
        categoryList=categoryDL().allCategories
        cate=[]
        for i in range(len(categoryList)):
            cate.append(categoryList[i].category)
        quan=[]
        for i in range(len(cate)):
            tSum=0
            for j in range(len(category)):                
                if category[j]==cate[i]:
                    tSum=tSum+int(quantity[j])
            quan.append(tSum)
        plt.figure(figsize=(20,4))
        plt.xlabel("Categories",fontsize=14)
        plt.ylabel("Quantities",fontsize=14)
        plt.bar(cate,quan,color='#48ACAC')
        plt.savefig("output.png", transparent=True)
        # pixmap=QPixmap("save_figure.png")
        # item = QGraphicsPixmapItem(pixmap)
        # scene.addItem(item)
        pixmap = QPixmap('output.png')
        self.lblWeeklyRevenue.setPixmap(pixmap)
        self.lblWeeklyRevenue.resize(pixmap.width(),pixmap.height())



 #Manager Account Details
    def accountDetails(self):
        self.txtName.setText("Ali Haider")
        self.txtID.setEnabled(False)
        self.txtName.setEnabled(False)
        self.txtCNIC.setEnabled(False)
        self.txtEmail.setEnabled(False)
        self.txtUserName.setEnabled(False)
        self.txtPassword.setEnabled(False)
        self.txtCellNo.setEnabled(False)
        self.txtSalary.setEnabled(False)
    def changeUserNameAndPassword(self):
        pass
        # self.c=ChangeUserNamePassword()
        # self.c.show()
        
        
        
       



#Product CRUD Functions
    def loadTableProduct(self):
        self.tableAdminProducts.setRowCount(0)
        self.tableAdminProducts.setColumnCount(0)
        self.tableAdminProducts.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        roww = 0
        self.tableAdminProducts.setRowCount(productDL().productCount)
        self.tableAdminProducts.setColumnCount(9)
        stylesheet = "::section{Background-color:#48ACAC;color:white;}"
        self.tableAdminProducts.horizontalHeader().setStyleSheet(stylesheet)
        self.tableAdminProducts.setHorizontalHeaderLabels(['Id', 'Name', 'Category', 'Description' , 'Quantity' , 'Productioin Cost', 'Sales Price','Date Added','Expiry Date'])
        self.tableAdminProducts.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        if(productDL.productList.head != None):
            start = productDL.productList.head 
            while start != None:
                row = start.getProduct()
                self.tableAdminProducts.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableAdminProducts.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.name)))
                self.tableAdminProducts.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.category)))
                self.tableAdminProducts.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row.description)))
                self.tableAdminProducts.setItem(roww, 4 , QtWidgets.QTableWidgetItem((str(row.quantity))))
                self.tableAdminProducts.setItem(roww, 5, QtWidgets.QTableWidgetItem((str(row.productionCost))))
                self.tableAdminProducts.setItem(roww, 6, QtWidgets.QTableWidgetItem((str(row.salePrice))))
                self.tableAdminProducts.setItem(roww, 7, QtWidgets.QTableWidgetItem((row.date)))
                self.tableAdminProducts.setItem(roww, 8, QtWidgets.QTableWidgetItem((row.expiryDate)))
                roww = roww + 1
                start = start.getNextNode()
    def addProduct(self):
        pass
        # self.addnewProduct = AddProductWindow()
        # self.addnewProduct.show()
        # self.addnewProduct.btnAdd.clicked.connect(lambda : self.loadTableProduct())
    def editProduct(self):
        if(self.tableAdminProducts.currentRow() != None and self.tableAdminProducts.currentRow()>=0):
            row = self.tableAdminProducts.currentRow()
            Id = self.tableAdminProducts.item(row,0).text()
            name = self.tableAdminProducts.item(row,1).text()
            category = self.tableAdminProducts.item(row,2).text()
            description = self.tableAdminProducts.item(row,3).text()
            quantity = self.tableAdminProducts.item(row,4).text()
            productionCost = self.tableAdminProducts.item(row,5).text()
            salePrice = self.tableAdminProducts.item(row,6).text()
            date = self.tableAdminProducts.item(row,7).text()
            expiryDate = self.tableAdminProducts.item(row,8).text()
            
            p = product(name, Id, category, quantity, description, productionCost, salePrice, date, expiryDate)
            # self.addnewProduct = EditProductWindow(p)
            # self.addnewProduct.show()
            # self.addnewProduct.btnAdd.clicked.connect(lambda : self.loadTableProduct())
    def deleteProduct(self):
        if(self.tableAdminProducts.currentRow() != None and self.tableAdminProducts.currentRow()>=0):
            qm =QMessageBox
            ret=qm.question(self,'', "Are you sure to delete this Delivery Man?", qm.Yes | qm.No)           
            if ret==qm.Yes:
                row = self.tableAdminProducts.currentRow()
                Id = self.tableAdminProducts.item(row,0).text()
                name = self.tableAdminProducts.item(row,1).text()
                category = self.tableAdminProducts.item(row,2).text()
                description = self.tableAdminProducts.item(row,3).text()
                quantity = self.tableAdminProducts.item(row,4).text()
                productionCost = self.tableAdminProducts.item(row,5).text()
                salePrice = self.tableAdminProducts.item(row,6).text()
                date = self.tableAdminProducts.item(row,7).text()
                expiryDate = self.tableAdminProducts.item(row,8).text()
                
                p = product(name, Id, category, quantity, description, productionCost, salePrice, date, expiryDate)
                productDL().deleteProduct(p)
                self.loadTableProduct()
                productDL().storeAllProductInFile(self.file_paths.ProductsInfo)
    def exportProductCSV(self):
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.Directory)
            if dialog.exec_():
                fileNames = dialog.selectedFiles()           
                files = [self.file_paths.ProductsInfo]
                for f in files:
                    shutil.copy(f,fileNames[0])
                    break
                msg = QMessageBox()
                msg.setText("Done")
                msg.setInformativeText('CSV Exported Successfully!')
                msg.setWindowTitle("Edited")
                msg.exec_()    


    #Sale Agent CRUD  
    def addNewAgent(self):
        self.newq=AddSaleAgentWindow()
        self.newq.show()
        self.newq.btnAdd.clicked.connect(lambda:self.loadSaleAgentData())
        self.loadingSaleAgentLabels() 
        
    def editDataSaleAgent(self):
        if(self.tableSaleAgentList.currentRow() != None and self.tableSaleAgentList.currentRow()>=0):
            row = self.tableSaleAgentList.currentRow()
            col = self.tableSaleAgentList.currentColumn()
            Id=self.tableSaleAgentList.item(row,0).text()
            role= self.tableSaleAgentList.item(row,1).text()
            userName = self.tableSaleAgentList.item(row,2).text()
            name = self.tableSaleAgentList.item(row,3).text()
            password = self.tableSaleAgentList.item(row,4).text()
            cnic = self.tableSaleAgentList.item(row,5).text()
            email = self.tableSaleAgentList.item(row,6).text()
            cellNo = self.tableSaleAgentList.item(row,7).text()
            dateCreated = self.tableSaleAgentList.item(row,8).text() 
            vehicle = self.tableSaleAgentList.item(row,9).text() 
            salary = self.tableSaleAgentList.item(row,10).text() 
            S = salesMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
            
            # self.editSaleAgentWindow=ManagerEditSaleAgent(S)
            # self.editSaleAgentWindow.show()
            # # self.loadSaleAgentData()
            # # salesManDL().addAllSalesmanToFile()
            # self.editSaleAgentWindow.btnSave.clicked.connect(lambda:self.loadSaleAgentData())
            # self.editSaleAgentWindow.btnSave.clicked.connect(lambda:salesManDL().addAllSalesmanToFile("SalesManInfo.csv"))
    def deleteSaleAgent(self):
       row = self.tableSaleAgentList.currentRow()
       print(row)
       if row>=0:
           qm =QMessageBox
           ret=qm.question(self,'', "Are you sure to delete this Sale Agent?", qm.Yes | qm.No)           
           if ret==qm.Yes:
               row = self.tableSaleAgentList.currentRow()
               col = self.tableSaleAgentList.currentColumn()
               Id=self.tableSaleAgentList.item(row,0).text()
               role= self.tableSaleAgentList.item(row,1).text()
               userName = self.tableSaleAgentList.item(row,2).text()
               name = self.tableSaleAgentList.item(row,3).text()
               password = self.tableSaleAgentList.item(row,4).text()
               cnic = self.tableSaleAgentList.item(row,5).text()
               email = self.tableSaleAgentList.item(row,6).text()
               cellNo = self.tableSaleAgentList.item(row,7).text()
               dateCreated = self.tableSaleAgentList.item(row,8).text() 
               vehicle = self.tableSaleAgentList.item(row,9).text() 
               salary = self.tableSaleAgentList.item(row,10).text() 
               S = salesMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
               salesManDL().deleteSaleAgent(S)
               self.loadSaleAgentData()
               salesManDL().addAllSalesmanToFile(self.file_paths.SalesManInfo)
               self.loadingSaleAgentLabels() 
    def exportSaleAgentData(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            files = [self.file_paths.SalesManInfo]
            for f in files:
                shutil.copy(f,fileNames[0])
                break
    
    
    def loadingSaleAgentLabels(self):
         self.lblTotalSaleAgent.setText(str(salesManDL.saleAgentCount))
         self.lblTotalAgentSalary.setText(salesManDL().allSaleAgentSalaries())
         self.lblVehicles.setText(str(salesManDL.saleAgentCount))
    
    def loadSaleAgentData(self):
        self.tableSaleAgentList.setRowCount(0)
        self.tableSaleAgentList.setColumnCount(0)
        self.tableSaleAgentList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # self.tableOrderDispatcherList.setColumnCount(5)
        # self.tableOrderDispatcherList.setRowCount(15)
        roww = 0
        self.tableSaleAgentList.setRowCount(salesManDL.saleAgentCount)
        self.tableSaleAgentList.setColumnCount(11)
        # self.tableSaleAgentList.setHorizontalHeaderLabels(['Delete', 'Edit','Category', 'Brand', 'Model', 'Price' , 'Processor' , 'Resolution', 'Ram' , 'Storage' , 'Screen Size'])
        self.tableSaleAgentList.horizontalHeader().setVisible(True)
        stylesheet = "::section{Background-color:#48ACAC;color:white;}"
        self.tableSaleAgentList.horizontalHeader().setStyleSheet(stylesheet)
        self.tableSaleAgentList.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
        self.tableSaleAgentList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        start=salesManDL().salesMan.head
        if start is None:
            print("Empty List")
        else:
            while start:
                row=start.getProduct()
        
            # return (salesAgent.Id,salesAgent.login.role,salesAgent.login.userName,salesAgent.name,salesAgent.login.password,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
            # self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableSaleAgentList.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableSaleAgentList.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
                self.tableSaleAgentList.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
                self.tableSaleAgentList.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
                self.tableSaleAgentList.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
                self.tableSaleAgentList.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
                self.tableSaleAgentList.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
                self.tableSaleAgentList.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
                self.tableSaleAgentList.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
                self.tableSaleAgentList.setItem(roww, 9 , QtWidgets.QTableWidgetItem((row.vehicle)))
                self.tableSaleAgentList.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
                roww = roww + 1
                start=start.getNextNode()
    
    
    
    
    
    
    #Order Dispatcher CRUD
    def addNewOrderDispatcher(self):
        pass
        # self.newq=ManagerAddingNewOrderDispacther()
        # self.newq.show()
        # self.newq.btnAdd.clicked.connect(lambda:self.loadOrderDispatcherData())
        # self.loadingODLabels()
    def editOD(self):
        if(self.tableOrderDispatcherList.currentRow() != None and self.tableOrderDispatcherList.currentRow()>=0):
            row = self.tableOrderDispatcherList.currentRow()
            col = self.tableOrderDispatcherList.currentColumn()
            Id=self.tableOrderDispatcherList.item(row,0).text()
            role= self.tableOrderDispatcherList.item(row,1).text()
            userName = self.tableOrderDispatcherList.item(row,2).text()
            name = self.tableOrderDispatcherList.item(row,3).text()
            password = self.tableOrderDispatcherList.item(row,4).text()
            cnic = self.tableOrderDispatcherList.item(row,5).text()
            email = self.tableOrderDispatcherList.item(row,6).text()
            cellNo = self.tableOrderDispatcherList.item(row,7).text()
            dateCreated = self.tableOrderDispatcherList.item(row,8).text() 
            salary = self.tableOrderDispatcherList.item(row,9).text() 
            S = orderDispatcher(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,salary)
            # self.editODWindow=ManagerEditOrderDispacther(S)
            # self.editODWindow.show()
            # # self.loadSaleAgentData()
            # # salesManDL().addAllSalesmanToFile()
            # self.editODWindow.btnSave.clicked.connect(lambda:self.loadOrderDispatcherData())
            # self.editODWindow.btnSave.clicked.connect(lambda:orderDispatcherDL().addAllODToFile("OrderDispatcherInfo.csv"))
    def deleteOD(self):
        row = self.tableOrderDispatcherList.currentRow()
        print(row)
        if row>=0:
            qm =QMessageBox
            ret=qm.question(self,'', "Are you sure to delete this Order Dispatcher?", qm.Yes | qm.No)           
            if ret==qm.Yes:
                row = self.tableOrderDispatcherList.currentRow()
                col = self.tableOrderDispatcherList.currentColumn()
                Id=self.tableOrderDispatcherList.item(row,0).text()
                role= self.tableOrderDispatcherList.item(row,1).text()
                userName = self.tableOrderDispatcherList.item(row,2).text()
                name = self.tableOrderDispatcherList.item(row,3).text()
                password = self.tableOrderDispatcherList.item(row,4).text()
                cnic = self.tableOrderDispatcherList.item(row,5).text()
                email = self.tableOrderDispatcherList.item(row,6).text()
                cellNo = self.tableOrderDispatcherList.item(row,7).text()
                dateCreated = self.tableOrderDispatcherList.item(row,8).text() 
                salary = self.tableOrderDispatcherList.item(row,9).text() 
                O = orderDispatcher(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,salary)
                orderDispatcherDL().deleteOrderDispatcher(O)
                self.loadOrderDispatcherData()
                orderDispatcherDL().addAllODToFile(self.file_paths.OrderDispatcherInfo)
                self.loadingODLabels()
    def exportOrderDispatcher(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        
            files = [self.file_paths.OrderDispatcherInfo]
            for f in files:
                shutil.copy(f,fileNames[0])
                break
            msg = QMessageBox()
            msg.setText("Done")
            msg.setInformativeText('CSV Exported Successfully!')
            msg.setWindowTitle("Edited")
            msg.exec_()
    def loadingODLabels(self):
        self.lblTotalOrderDispatcher.setText(str(orderDispatcherDL.oderDispactherCount))
        self.lblTotalOrderDispatcherSalary.setText(orderDispatcherDL().allODSalaries())
        # self.lblVehicles.setText(str(salesManDL.salesMan.length()))   
    def loadOrderDispatcherData(self):
        self.tableOrderDispatcherList.setRowCount(0)
        self.tableOrderDispatcherList.setColumnCount(0)
        # self.tableOrderDispatcherList.setColumnCount(5)
        # self.tableOrderDispatcherList.setRowCount(15)
        self.tableOrderDispatcherList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableOrderDispatcherList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        roww = 0
        self.tableOrderDispatcherList.setRowCount(orderDispatcherDL().oderDispactherCount)
        self.tableOrderDispatcherList.setColumnCount(10)
        # self.tableSaleAgentList.setHorizontalHeaderLabels(['Delete', 'Edit','Category', 'Brand', 'Model', 'Price' , 'Processor' , 'Resolution', 'Ram' , 'Storage' , 'Screen Size'])
        self.tableOrderDispatcherList.horizontalHeader().setVisible(True)
        stylesheet = "::section{Background-color:#48ACAC;color:white;}"
        self.tableOrderDispatcherList.horizontalHeader().setStyleSheet(stylesheet)
        self.tableOrderDispatcherList.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Salary'])
        start=orderDispatcherDL.orderDispatcherLinkedList.head
        if start is None:
            print("Empty List")
        else:
            while start:
                row=start.getProduct()        
            # return (salesAgent.Id,salesAgent.login.role,salesAgent.login.userName,salesAgent.name,salesAgent.login.password,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
            # self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableOrderDispatcherList.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableOrderDispatcherList.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
                self.tableOrderDispatcherList.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
                self.tableOrderDispatcherList.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
                self.tableOrderDispatcherList.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
                self.tableOrderDispatcherList.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
                self.tableOrderDispatcherList.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
                self.tableOrderDispatcherList.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
                self.tableOrderDispatcherList.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))            
                self.tableOrderDispatcherList.setItem(roww, 9 , QtWidgets.QTableWidgetItem((row.salary)))
                roww = roww + 1
                start=start.getNextNode()
    
    
    
    #Delivery Man CRUD
    def addNewDM(self):
        pass
        # self.newq=ManagerAddingNewDeliveryMan()
        # self.newq.show()
        # self.newq.btnAdd.clicked.connect(lambda:self.loadDMData())
        # self.loadingDMLabels()
    def editDM(self):
        if(self.tableSaleAgentList_2.currentRow() != None and self.tableSaleAgentList_2.currentRow()>=0 ):

            row = self.tableSaleAgentList_2.currentRow()
            col = self.tableSaleAgentList_2.currentColumn()
            Id=self.tableSaleAgentList_2.item(row,0).text()
            role= self.tableSaleAgentList_2.item(row,1).text()
            userName = self.tableSaleAgentList_2.item(row,2).text()
            name = self.tableSaleAgentList_2.item(row,3).text()
            password = self.tableSaleAgentList_2.item(row,4).text()
            cnic = self.tableSaleAgentList_2.item(row,5).text()
            email = self.tableSaleAgentList_2.item(row,6).text()
            cellNo = self.tableSaleAgentList_2.item(row,7).text()
            dateCreated = self.tableSaleAgentList_2.item(row,8).text() 
            vehicle = self.tableSaleAgentList_2.item(row,9).text() 
            salary = self.tableSaleAgentList_2.item(row,10).text() 
            d = deliveryMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
            # self.editDMWindow=ManagerEditDeliveryMan(d)
            # self.editDMWindow.show()
            # # self.loadSaleAgentData()
            # # salesManDL().addAllSalesmanToFile()
            # self.editDMWindow.btnSave.clicked.connect(lambda:self.loadDMData())
            # self.editDMWindow.btnSave.clicked.connect(lambda:deliveryManDL().addAllDMToFile("DeliveryManInfo.csv"))    
    
    def deleteDM(self):
        row = self.tableSaleAgentList_2.currentRow()
        print(row)
        if row>=0:
            qm =QMessageBox
            ret=qm.question(self,'', "Are you sure to delete this Delivery Man?", qm.Yes | qm.No)           
            if ret==qm.Yes:
                row = self.tableSaleAgentList_2.currentRow()
                col = self.tableSaleAgentList_2.currentColumn()
                Id=self.tableSaleAgentList_2.item(row,0).text()
                role= self.tableSaleAgentList_2.item(row,1).text()
                userName = self.tableSaleAgentList_2.item(row,2).text()
                name = self.tableSaleAgentList_2.item(row,3).text()
                password = self.tableSaleAgentList_2.item(row,4).text()
                cnic = self.tableSaleAgentList_2.item(row,5).text()
                email = self.tableSaleAgentList_2.item(row,6).text()
                cellNo = self.tableSaleAgentList_2.item(row,7).text()
                dateCreated = self.tableSaleAgentList_2.item(row,8).text() 
                vehicle = self.tableSaleAgentList_2.item(row,9).text() 
                salary = self.tableSaleAgentList_2.item(row,10).text() 
                d = deliveryMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
                deliveryManDL().deleteDeliveryMan(d)
                self.loadDMData()
                deliveryManDL().addAllDMToFile(self.file_paths.DeliveryManInfo)
                self.loadingDMLabels()
    
    def exportDeliveryMan(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        # print(fileNames[0])
            files = [self.file_paths.DeliveryManInfo]
            for f in files:
                shutil.copy(f,fileNames[0])
                break
            msg = QMessageBox()
            msg.setText("Done")
            msg.setInformativeText('CSV Exported Successfully!')
            msg.setWindowTitle("Edited")
            msg.exec_()
    def loadingDMLabels(self):
        self.lblTotalDeliveryMen.setText(str(deliveryManDL.deliveryManCount))
        self.lblTotalDeliveryMenSalary.setText(deliveryManDL().allDMSalaries())
        # self.lblVehicles.setText(str(salesManDL.salesMan.length()))   
    def loadDMData(self):
        self.tableSaleAgentList_2.setRowCount(0)
        self.tableSaleAgentList_2.setColumnCount(0)
        self.tableSaleAgentList_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        stylesheet = "::section{Background-color:#48ACAC;color:white;}"
        self.tableSaleAgentList_2.horizontalHeader().setStyleSheet(stylesheet)
        self.tableSaleAgentList_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # self.tableOrderDispatcherList.setColumnCount(5)
        # self.tableOrderDispatcherList.setRowCount(15)
        roww = 0
        self.tableSaleAgentList_2.setRowCount(deliveryManDL.deliveryManCount)
        self.tableSaleAgentList_2.setColumnCount(11)
        # self.tableSaleAgentList.setHorizontalHeaderLabels(['Delete', 'Edit','Category', 'Brand', 'Model', 'Price' , 'Processor' , 'Resolution', 'Ram' , 'Storage' , 'Screen Size'])
        self.tableSaleAgentList_2.horizontalHeader().setVisible(True)
        self.tableSaleAgentList_2.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
        start=deliveryManDL().deliveryManLinkedList.head
        if start is None:
            print("Empty List")
        else:
            while start:
                row=start.getProduct()
            
            # return (salesAgent.Id,salesAgent.login.role,salesAgent.login.userName,salesAgent.name,salesAgent.login.password,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
            # self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableSaleAgentList_2.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableSaleAgentList_2.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
                self.tableSaleAgentList_2.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
                self.tableSaleAgentList_2.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
                self.tableSaleAgentList_2.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
                self.tableSaleAgentList_2.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
                self.tableSaleAgentList_2.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
                self.tableSaleAgentList_2.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
                self.tableSaleAgentList_2.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
                self.tableSaleAgentList_2.setItem(roww, 9 , QtWidgets.QTableWidgetItem((row.vehicle)))
                self.tableSaleAgentList_2.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
                roww = roww + 1
                start=start.getNextNode()
    
   #Vehicle CRUD
    def addVehicle(self):
        pass
        # self.newq=ManagerAddVehicle()
        # self.newq.show()
        # self.newq.btnAdd.clicked.connect(lambda:self.loadVehicleData())
        # self.loadingVehicleLabels()
    def EditVehicle(self):
         
         if self.tableSaleAgentList_4.currentRow() != None and self.tableSaleAgentList_4.currentRow()>=0:
             row = self.tableSaleAgentList_4.currentRow()
             col = self.tableSaleAgentList_4.currentColumn()
             Id=self.tableSaleAgentList_4.item(row,0).text()
             name= self.tableSaleAgentList_4.item(row,1).text()
             brand = self.tableSaleAgentList_4.item(row,2).text()
             category = self.tableSaleAgentList_4.item(row,3).text()
             capacity = self.tableSaleAgentList_4.item(row,4).text()
             number = self.tableSaleAgentList_4.item(row,5).text()
             price = self.tableSaleAgentList_4.item(row,6).text()
             datePresent = self.tableSaleAgentList_4.item(row,7).text()
             v = vehicle(Id,name,brand,category ,capacity, number,price, datePresent) 
             # self.editVehicleWindow=ManagerEditVehicle(v)
             # self.editVehicleWindow.show()
             # # self.loadSaleAgentData()
             # # salesManDL().addAllSalesmanToFile()
             # self.editVehicleWindow.btnSave.clicked.connect(lambda:self.loadVehicleData())
             # self.editVehicleWindow.btnSave.clicked.connect(lambda:vehicleDL().addAllVehicleToFile("VehicleInfo.csv"))
    def deleteVehicle(self):
        row = self.tableSaleAgentList_4.currentRow()
        print(row)
        if row>=0:
            qm =QMessageBox
            ret=qm.question(self,'', "Are you sure to delete this Vehicle?", qm.Yes | qm.No)           
            if ret==qm.Yes:
                row = self.tableSaleAgentList_4.currentRow()
                col = self.tableSaleAgentList_4.currentColumn()
                Id= self.tableSaleAgentList_4.item(row,0).text()
                name = self.tableSaleAgentList_4.item(row,1).text()
                brand = self.tableSaleAgentList_4.item(row,2).text()
                category = self.tableSaleAgentList_4.item(row,3).text()
                capacity = self.tableSaleAgentList_4.item(row,4).text()
                number = self.tableSaleAgentList_4.item(row,5).text()
                price = self.tableSaleAgentList_4.item(row,6).text()
                datePresent = self.tableSaleAgentList_4.item(row,7).text()       
                v = vehicle(Id,name,brand,category ,capacity, number,price, datePresent) 
                vehicleDL().deleteVehicle(v)
                self.loadVehicleData()
                vehicleDL().addAllVehicleToFile(self.file_paths.VehicleInfo)                
                self.loadingVehicleLabels()
    def exportVehicle(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        # print(fileNames[0])
            files = [self.file_paths.VehicleInfo]
            for f in files:
                shutil.copy(f,fileNames[0])
                break
            msg = QMessageBox()
            msg.setText("Done")
            msg.setInformativeText('CSV Exported Successfully!')
            msg.setWindowTitle("Edited")
            msg.exec_()
    def loadingVehicleLabels(self):
        self.lblManagerTotalVehicles.setText(str(vehicleDL().vehicleCount))
        # self.lblTotalDeliveryMenSalary.setText(deliveryManDL().allDMSalaries())    

    def loadVehicleData(self):
        self.tableSaleAgentList_4.setRowCount(0)
        self.tableSaleAgentList_4.setColumnCount(0)
        self.tableSaleAgentList_4.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        roww = 0
        self.tableSaleAgentList_4.setRowCount(vehicleDL().vehicleCount)
        self.tableSaleAgentList_4.setColumnCount(8)
        self.tableSaleAgentList_4.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # self.tableSaleAgentList.setHorizontalHeaderLabels(['Delete', 'Edit','Category', 'Brand', 'Model', 'Price' , 'Processor' , 'Resolution', 'Ram' , 'Storage' , 'Screen Size'])
        self.tableSaleAgentList_4.horizontalHeader().setVisible(True)
        self.tableSaleAgentList_4.setHorizontalHeaderLabels(['ID', 'Name', 'Brand', 'Category' , 'Capacity' , 'Number', 'Price', 'Date Entry'])
        stylesheet = "::section{Background-color:#48ACAC;color:white;}"
        self.tableSaleAgentList_4.horizontalHeader().setStyleSheet(stylesheet)
        start=vehicleDL().vehicleLinkedList.head
        if start is None:
            print("Empty List")
        else:
            while start:
                row=start.getProduct()
        
            # return (salesAgent.Id,salesAgent.login.role,salesAgent.login.userName,salesAgent.name,salesAgent.login.password,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
            # self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableSaleAgentList_4.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableSaleAgentList_4.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.name)))
                self.tableSaleAgentList_4.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.brand)))
                self.tableSaleAgentList_4.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.category))))
                self.tableSaleAgentList_4.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.category)))
                self.tableSaleAgentList_4.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.capacity)))
                self.tableSaleAgentList_4.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.number)))
                self.tableSaleAgentList_4.setItem(roww, 7 , QtWidgets.QTableWidgetItem((str(row.dateCreated))  ))             
                roww = roww + 1
                start=start.getNextNode()