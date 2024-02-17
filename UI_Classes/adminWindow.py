# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 01:26:51 2024

@author: Digital Zone
"""

import os
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from UI_Classes.adminWindow_ui import Ui_MainWindow
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

class AdminWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        # Set up the user interface from the generated class
        self.setupUi(self)
        # Set flags to remove the default title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))       
        self.stackedWidget.setCurrentWidget(self.AdminDashboard)
        self.btnAdminDashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AdminDashboard))
        self.btnAdminOrder.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AdminOrderPage))
        self.btnAdminProduct.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AdminProductPage))
        self.btnAdminEmployee.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AdminEmployeePage))
        self.btnAdminVehicle.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AdminVehiclePage))
        self.btnAdminReport.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AdminReport))
        self.loadProductGraph()
        self.btnAdminDashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.loadProductGraph()))
        
        self.loadAllEmployeesGraph()
        self.btnPrint.clicked.connect(lambda: self.printProductGraph())
        self.btnAdminReport.clicked.connect(lambda: self.loadReports())
        self.btnAdminDashboard.clicked.connect(lambda: self.loadAllEmployeesGraph())   
        self.btnPrintGraphPerDay.clicked.connect(lambda: self.printLast7DaySaleReports())
        self.btnAdminGenerateReport.clicked.connect(lambda: self.generateReportPage())
       
        #Product CRUD
        self.btnAdminProduct.clicked.connect(lambda: self.loadTableProduct())
        self.btnAdminAddProduct.clicked.connect(lambda: self.loadTableProduct())
        self.btnAdminAddProduct.clicked.connect(lambda: self.addProduct())
        self.btnAdminDeleteProduct.clicked.connect(lambda: self.deleteProduct())
        self.btnAdminEditProduct.clicked.connect(lambda: self.editProduct())
        self.btnAdminProductCSV.clicked.connect(lambda: self.exportProductCSV())
        
        #Employee CRUD
        self.btnAdminEmployee.clicked.connect(lambda: self.loadEmployeeTable())
        self.btnAdminEditEmployees.clicked.connect(lambda: self.editEmployee())
        self.btnAdminDeleteEmployees.clicked.connect(lambda: self.deleteEmployee())
        self.btnAdminEmployeeCSV.clicked.connect(lambda: self.exportCSVPDFEmployee())
        self.btnAdminEmployee.clicked.connect(lambda: self.loadLabels())
        self.cmbxAdminAddEmployee.activated.connect(lambda: self.addUser())
        self.cmbxAdminViewEmployees.activated.connect(lambda: self.viewUser())
     
        
        #Vehicle CRUD
        self.btnAdminVehicle.clicked.connect(lambda: self.loadVehicleTable())
        self.btnAdminAddVehicle.clicked.connect(lambda: self.addVehicle())
        self.btnAdminEditVehicle.clicked.connect(lambda: self.editVehicle())
        self.btnAdminDeleteVehicle.clicked.connect(lambda: self.deleteVehicle())
        self.btnAdminVehicleCSV.clicked.connect(lambda: self.exportVehicle())
       
    
    def generateReportPage(self):
        pass
        # self.geneReport=GenerateReport()
        # self.geneReport.show()
        
    
    
    
    def printLast7DaySaleReports(self):
        df=pd.read_csv(self.file_paths.SalesPerDate,header=None,usecols=[0,1],infer_datetime_format=True)
        sales=df[0].values.tolist()
        dates=df[1].values.tolist()
        sa=[]
        da=[]
        today = date.today()
        for i in range(7):
            yesterday =(today - timedelta(days = i+1)).strftime("%d/%m/%Y")
            tSum=0
            for j in range(len(dates)):
                if dates[j]==str(yesterday):
                    tSum=tSum+int(sales[j])
            
            sa.append(tSum) 
            da.append(yesterday)
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            add=fileNames[0]+"/SalesInLast7Days.pdf"
            with PdfPages(add) as export_pdf:
                plt.figure(figsize=(10,6))
                plt.xlabel("Date",fontsize=14)
                plt.ylabel("Sales",fontsize=14)
                plt.bar(da,sa,color='#48ACAC')
                # plt.grid(True)
                export_pdf.savefig()
                plt.close()
        
    
    
    def loadReports(self):
        df=pd.read_csv(self.file_paths.SalesPerDate,header=None,usecols=[0,1],infer_datetime_format=True)
        sales=df[0].values.tolist()
        dates=df[1].values.tolist()
        sa=[]
        da=[]
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
        self.label_43.setText(str(bestDay))
        self.label_53.setText(str(bestSale))
        self.label_52.setText(str(worstDay))
        self.label_54.setText(str(worstSale))
        plt.figure(figsize=(10,5))
        plt.xlabel("Date",fontsize=14)
        plt.ylabel("Sales",fontsize=14)
        plt.bar(da,sa,color='#48ACAC')
        plt.savefig("salesLast7Days.png", transparent=True)
        # pixmap=QPixmap("save_figure.png")
        # item = QGraphicsPixmapItem(pixmap)
        # scene.addItem(item)
        pixmap = QPixmap('salesLast7Days.png')        
        self.lblSalePerDay.setPixmap(pixmap)
    
    def loadAllEmployeesGraph(self):
        employees=["Manager","Sales Agent","Order Dispatcher","Delivery Man"]
        num=[]
        num.append(managerDL().managerCount)
        num.append(salesManDL().saleAgentCount)
        num.append(orderDispatcherDL().oderDispactherCount)
        num.append(deliveryManDL().deliveryManCount)
        colors = ['#8CDBA9','#4E9C81','#49DCB1','#00917C']
        plt.figure(figsize=(8,6))
        explode = (0, 0.1, 0, 0)       
        fig1, ax1 = plt.subplots()
        ax1.pie(num, explode=explode, labels=employees,colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')        
        plt.savefig("allEmployeesGraph.png", transparent=True)
        plt.show()
        print("Ali")
        # pixmap=QPixmap("save_figure.png")
        # item = QGraphicsPixmapItem(pixmap)
        # scene.addItem(item)
        pixmap = QPixmap('allEmployeesGraph.png')
        self.lblEmployeesGraph.setPixmap(pixmap)
    
    def printProductGraph(self):
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
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            add=fileNames[0]+"/products.pdf"
            with PdfPages(add) as export_pdf:
                plt.figure(figsize=(10,6))
                plt.xlabel("Categories",fontsize=14)
                plt.ylabel("Quantities",fontsize=14)
                plt.bar(cate,quan,color='#48ACAC')
                # plt.grid(True)
                export_pdf.savefig()
                plt.close()
        
    
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
        plt.figure(figsize=(10,6))
        plt.xlabel("Categories",fontsize=14)
        plt.ylabel("Quantities",fontsize=14)
        plt.bar(cate,quan,color='#48ACAC')
        plt.savefig("output.png", transparent=True)
        # pixmap=QPixmap("save_figure.png")
        # item = QGraphicsPixmapItem(pixmap)
        # scene.addItem(item)
        pixmap = QPixmap('output.png')
        self.labelProduct.setPixmap(pixmap)
        self.labelProduct.resize(pixmap.width(),pixmap.height())
        
        
    
    #Employee Window
    def addUser(self):
        u = self.cmbxAdminAddEmployee.currentText()
        # if u=="Manager":
        #     self.S=AddNewManager()
        #     self.S.show()
        #     self.S.btnAdd.clicked.connect(lambda : self.loadEmployeeTable())
        #     self.S.btnAdd.clicked.connect(lambda: self.loadLabels())
    
        # elif u=="Sales Agent":
        #     self.S=ManagerAddingNewSaleAgent()
        #     self.S.show()
        #     self.S.btnAdd.clicked.connect(lambda : self.loadEmployeeTable())
        #     self.S.btnAdd.clicked.connect(lambda: self.loadLabels())
        # elif u=="Order Dispatcher":
        #     self.S=ManagerAddingNewOrderDispacther()
        #     self.S.show()
        #     self.S.btnAdd.clicked.connect(lambda : self.loadEmployeeTable())
        #     self.S.btnAdd.clicked.connect(lambda: self.loadLabels())
        # elif u=="Delivery Man":
        #     self.S=ManagerAddingNewDeliveryMan()
        #     self.S.show()
        #     self.S.btnAdd.clicked.connect(lambda : self.loadEmployeeTable())
        #     self.S.btnAdd.clicked.connect(lambda: self.loadLabels())
            
    def viewUser(self):
        self.tableAdminEmployees.setRowCount(0)
        self.tableAdminEmployees.setColumnCount(0)   
        u = self.cmbxAdminViewEmployees.currentText()
        print("u",u)
        if u=="All" or u=="View Employees":
            self.loadEmployeeTable()
        elif u=="Sales Agent":
            count=salesManDL.saleAgentCount
            print("Ali")
            self.tableAdminEmployees.setRowCount(count)
            self.tableAdminEmployees.setColumnCount(11)    
            self.tableAdminEmployees.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableAdminEmployees.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            stylesheet = "::section{Background-color:#48ACAC;color:white;}"
            self.tableAdminEmployees.horizontalHeader().setStyleSheet(stylesheet)
            # self.tableAdminEmployees.Header.setStretchLastSection(True)
            self.tableAdminEmployees.horizontalHeader().setVisible(True)
            self.tableAdminEmployees.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
            if(salesManDL.salesMan.head != None):
                count=salesManDL.saleAgentCount
                roww=0
                # self.tableAdminEmployees.Header.setStretchLastSection(True)
                self.tableAdminEmployees.horizontalHeader().setVisible(True)
                self.tableAdminEmployees.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
                start = salesManDL.salesMan.head 
                while start != None:
                    row = start.getProduct()
                    print("Ali")
                    self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                    self.tableAdminEmployees.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
                    self.tableAdminEmployees.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
                    self.tableAdminEmployees.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
                    self.tableAdminEmployees.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
                    self.tableAdminEmployees.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
                    self.tableAdminEmployees.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
                    self.tableAdminEmployees.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
                    self.tableAdminEmployees.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
                    self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem((row.salary)))
                    self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem(row.vehicle))
                    self.tableAdminEmployees.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
                    roww = roww + 1
                    start = start.getNextNode()
            
        elif u=="Manager":
            count=managerDL.managerCount
            print("Ali")
            self.tableAdminEmployees.setRowCount(count)
            self.tableAdminEmployees.setColumnCount(11)    
            self.tableAdminEmployees.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            stylesheet = "::section{Background-color:#48ACAC;color:white;}"
            self.tableAdminEmployees.horizontalHeader().setStyleSheet(stylesheet)
            # self.tableAdminEmployees.Header.setStretchLastSection(True)
            self.tableAdminEmployees.horizontalHeader().setVisible(True)
            self.tableAdminEmployees.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
    
            self.tableAdminEmployees.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
            if(managerDL.managers.head != None):
                count=managerDL.managers
                roww=0
                # self.tableAdminEmployees.Header.setStretchLastSection(True)
               
                start = managerDL.managers.head 
                while start != None:
                    row = start.getProduct()
                    print("Ali")
                    self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                    self.tableAdminEmployees.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
                    self.tableAdminEmployees.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
                    self.tableAdminEmployees.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
                    self.tableAdminEmployees.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
                    self.tableAdminEmployees.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
                    self.tableAdminEmployees.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
                    self.tableAdminEmployees.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
                    self.tableAdminEmployees.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
                    self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem("N/A"))
                    self.tableAdminEmployees.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
                    roww = roww + 1
                    start = start.getNextNode()
        elif u=="Order Dispatcher":
            count=orderDispatcherDL.oderDispactherCount
            roww=0
            self.tableAdminEmployees.setRowCount(count)
            self.tableAdminEmployees.setColumnCount(11)    
            self.tableAdminEmployees.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            stylesheet = "::section{Background-color:#48ACAC;color:white;}"
            self.tableAdminEmployees.horizontalHeader().setStyleSheet(stylesheet)
            # self.tableAdminEmployees.Header.setStretchLastSection(True)
            self.tableAdminEmployees.horizontalHeader().setVisible(True)
            self.tableAdminEmployees.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
    
            self.tableAdminEmployees.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
            if orderDispatcherDL.orderDispatcherLinkedList.head !=None:
                start = orderDispatcherDL.orderDispatcherLinkedList.head 
                while start != None:
                    row = start.getProduct()
                    self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                    self.tableAdminEmployees.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
                    self.tableAdminEmployees.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
                    self.tableAdminEmployees.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
                    self.tableAdminEmployees.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
                    self.tableAdminEmployees.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
                    self.tableAdminEmployees.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
                    self.tableAdminEmployees.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
                    self.tableAdminEmployees.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
                    self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem("N/A"))
                    self.tableAdminEmployees.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
                    roww = roww + 1
                    start = start.getNextNode()
        elif u=="Delivery Man":
            count=deliveryManDL.deliveryManCount
            roww=0
            self.tableAdminEmployees.setRowCount(count)
            self.tableAdminEmployees.setColumnCount(11)    
            self.tableAdminEmployees.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableAdminEmployees.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
    
            # self.tableAdminEmployees.Header.setStretchLastSection(True)
            self.tableAdminEmployees.horizontalHeader().setVisible(True)
            stylesheet = "::section{Background-color:#48ACAC;color:white;}"
            self.tableAdminEmployees.horizontalHeader().setStyleSheet(stylesheet)
            self.tableAdminEmployees.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
            if deliveryManDL.deliveryManLinkedList.head !=None:
                start = deliveryManDL.deliveryManLinkedList.head 
                while start != None:
                    row = start.getProduct()
                    self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                    self.tableAdminEmployees.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
                    self.tableAdminEmployees.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
                    self.tableAdminEmployees.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
                    self.tableAdminEmployees.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
                    self.tableAdminEmployees.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
                    self.tableAdminEmployees.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
                    self.tableAdminEmployees.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
                    self.tableAdminEmployees.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
                    self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem((row.vehicle)))
                    self.tableAdminEmployees.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
                    roww = roww + 1
                    start = start.getNextNode()
        
    
    
    
    
    
    
    #Product CRUD Functions
    def loadTableProduct(self):
            self.tableAdminProducts.setRowCount(0)
            self.tableAdminProducts.setColumnCount(0)
            self.tableAdminProducts.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    
            roww = 0
            self.tableAdminProducts.setRowCount(productDL().productCount)
            self.tableAdminProducts.setColumnCount(9)            
            self.tableAdminProducts.setHorizontalHeaderLabels(['Id', 'Name', 'Category', 'Description' , 'Quantity' , 'Productioin Cost', 'Sales Price','Date Added','Expiry Date'])
            stylesheet = "::section{Background-color:#48ACAC;color:white;}"
            self.tableAdminProducts.horizontalHeader().setStyleSheet(stylesheet)
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
    
    
    #Employee CRUD Function 
    def loadEmployeeTable(self):
       self.tableAdminEmployees.setRowCount(0)
       self.tableAdminEmployees.setColumnCount(0)
       roww = 0
       count=deliveryManDL.deliveryManCount+orderDispatcherDL.oderDispactherCount+salesManDL.saleAgentCount+managerDL.managerCount
       print(count)
       self.tableAdminEmployees.setRowCount(count)
       self.tableAdminEmployees.setColumnCount(11)    
       self.tableAdminEmployees.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
       
       # self.tableAdminEmployees.Header.setStretchLastSection(True)
       self.tableAdminEmployees.horizontalHeader().setVisible(True)
       stylesheet = "::section{Background-color:#48ACAC;color:white;}"
       self.tableAdminEmployees.horizontalHeader().setStyleSheet(stylesheet)
       self.tableAdminEmployees.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
    
       self.tableAdminEmployees.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
       if(managerDL.managers.head != None):
           count=managerDL.managers
           roww=0
           # self.tableAdminEmployees.Header.setStretchLastSection(True)
           self.tableAdminEmployees.horizontalHeader().setVisible(True)
           self.tableAdminEmployees.setHorizontalHeaderLabels(['ID', 'Role', 'User Name', 'Name' , 'Password' , 'CNIC', 'Email', 'Cell No', 'Date Entry', 'Vehicle', 'Salary'])
           start = managerDL.managers.head 
           while start != None:
               row = start.getProduct()
               print("Ali")
               self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
               self.tableAdminEmployees.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
               self.tableAdminEmployees.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
               self.tableAdminEmployees.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
               self.tableAdminEmployees.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
               self.tableAdminEmployees.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
               self.tableAdminEmployees.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
               self.tableAdminEmployees.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
               self.tableAdminEmployees.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
               self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem("N/A"))
               self.tableAdminEmployees.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
               roww = roww + 1
               start = start.getNextNode()
       if(salesManDL.salesMan.head != None):
           start = salesManDL.salesMan.head 
           while start != None:
               row = start.getProduct()
               print("Ali")
               self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
               self.tableAdminEmployees.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
               self.tableAdminEmployees.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
               self.tableAdminEmployees.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
               self.tableAdminEmployees.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
               self.tableAdminEmployees.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
               self.tableAdminEmployees.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
               self.tableAdminEmployees.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
               self.tableAdminEmployees.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
               self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem((row.vehicle)))
               self.tableAdminEmployees.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
               roww = roww + 1
               start = start.getNextNode()
       if deliveryManDL.deliveryManLinkedList.head !=None:
           start = deliveryManDL.deliveryManLinkedList.head 
           while start != None:
               row = start.getProduct()
               self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
               self.tableAdminEmployees.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
               self.tableAdminEmployees.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
               self.tableAdminEmployees.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
               self.tableAdminEmployees.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
               self.tableAdminEmployees.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
               self.tableAdminEmployees.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
               self.tableAdminEmployees.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
               self.tableAdminEmployees.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
               self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem((row.vehicle)))
               self.tableAdminEmployees.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
               roww = roww + 1
               start = start.getNextNode()
       if orderDispatcherDL.orderDispatcherLinkedList.head !=None:
           start = orderDispatcherDL.orderDispatcherLinkedList.head 
           while start != None:
               row = start.getProduct()
               self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
               self.tableAdminEmployees.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.login.role)))
               self.tableAdminEmployees.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.login.userName)))
               self.tableAdminEmployees.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.name))))
               self.tableAdminEmployees.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.login.password)))
               self.tableAdminEmployees.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.cnic)))
               self.tableAdminEmployees.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.email)))
               self.tableAdminEmployees.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row.cellNo)))
               self.tableAdminEmployees.setItem(roww, 8 , QtWidgets.QTableWidgetItem((str(row.dateCreated))))
               self.tableAdminEmployees.setItem(roww, 9 , QtWidgets.QTableWidgetItem("N/A"))
               self.tableAdminEmployees.setItem(roww, 10 , QtWidgets.QTableWidgetItem((row.salary)))
               roww = roww + 1
               start = start.getNextNode()
    def exportCSVPDFEmployee(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        # print(fileNames[0])
            files = [self.file_paths.ManagerInfo]
            for f in files:
                shutil.copy(f,fileNames[0])
                break
            msg = QMessageBox()
            msg.setText("Done")
            msg.setInformativeText('CSV Exported Successfully!')
            msg.setWindowTitle("Edited")
            msg.exec_()
       
    def editEmployee(self):
      if(self.tableAdminEmployees.currentRow() != None and self.tableAdminEmployees.currentRow()>=0):
           row = self.tableAdminEmployees.currentRow()
           role = self.tableAdminEmployees.item(row,1).text()       
           Id = self.tableAdminEmployees.item(row,0).text()
           userName = self.tableAdminEmployees.item(row,2).text()
           name = self.tableAdminEmployees.item(row,3).text()
           password = self.tableAdminEmployees.item(row,4).text()
           cnic = self.tableAdminEmployees.item(row,5).text()
           email = self.tableAdminEmployees.item(row,6).text()
           cellNo = self.tableAdminEmployees.item(row,7).text()
           dateCreated = self.tableAdminEmployees.item(row,8).text()          
           vehicle= self.tableAdminEmployees.item(row,9).text()
           salary = self.tableAdminEmployees.item(row,10).text()
           # if role=="Sales Agent":
           #     s=salesMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
           #     editWin=ManagerEditSaleAgent(s)
           #     editWin.show()
           #     self.S.btnSave.clicked.connect(lambda : self.loadEmployeeTable())
    
           # elif role=="Delivery Man":
           #     d=deliveryMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
           #     editWin=ManagerEditDeliveryMan(d)
           #     editWin.show()
           #     self.S.btnSave.clicked.connect(lambda : self.loadEmployeeTable())
    
           # elif role=="Order Dispatcher":
           #     o=orderDispatcher(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,salary)
           #     editWin=ManagerEditOrderDispacther(o)
           #     editWin.show()
           #     self.S.btnSave.clicked.connect(lambda : self.loadEmployeeTable())
    
           # elif role=="Manager":
           #     m=manager(userName, password, role, name, cnic, email, cellNo, Id, dateCreated, salary)
           #     editWin=EditManager(m)
           #     editWin.show()
           #     self.S.btnAdd.clicked.connect(lambda : self.loadEmployeeTable())
    def deleteEmployee(self):
      if(self.tableAdminEmployees.currentRow() != None and self.tableAdminEmployees.currentRow()>=0):
         qm =QMessageBox
         ret=qm.question(self,'', "Are you sure to delete this ?", qm.Yes | qm.No)           
         if ret==qm.Yes:
              row = self.tableAdminEmployees.currentRow()
              role = self.tableAdminEmployees.item(row,1).text()       
              Id = self.tableAdminEmployees.item(row,0).text()
              userName = self.tableAdminEmployees.item(row,2).text()
              name = self.tableAdminEmployees.item(row,3).text()
              password = self.tableAdminEmployees.item(row,4).text()
              cnic = self.tableAdminEmployees.item(row,5).text()
              email = self.tableAdminEmployees.item(row,6).text()
              cellNo = self.tableAdminEmployees.item(row,7).text()
              dateCreated = self.tableAdminEmployees.item(row,8).text()          
              vehicle= self.tableAdminEmployees.item(row,9).text()
              salary = self.tableAdminEmployees.item(row,10).text()
              if role=="Sales Agent":
                  s=salesMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
                  salesManDL.deleteSaleAgent(s)
                  salesManDL.addAllSalesmanToFile(self.file_paths.SalesManInfo)
                  
              elif role=="Delivery Man":
                  d=deliveryMan(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,vehicle,salary)
                  deliveryManDL().deleteDeliveryMan(d)
                  deliveryManDL.addAllDMToFile(self.file_paths.DeliveryManInfo)
              elif role=="Order Dispatcher":
                  o=orderDispatcher(userName, password,role,name ,cnic ,email, cellNo,Id, dateCreated,salary)
                  orderDispatcherDL.deleteOrderDispatcher(o)
                  orderDispatcherDL().addAllODToFile(self.file_paths.OrderDispatcherInfo)
              elif role=="Manager":
                  m=manager(userName, password, role, name, cnic, email, cellNo, Id, dateCreated, salary)
                  managerDL().deleteManager(m)
                  managerDL().addAllManagerToFile(self.file_paths.ManagerInfo)
              self.loadLabels()
              self.loadEmployeeTable()
       
    
       
    
       #Vehicle CRUD Functions
    def loadVehicleTable(self):
        self.tableAdminEmployees_2.setRowCount(0)
        self.tableAdminEmployees_2.setColumnCount(0)
        self.tableAdminEmployees_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    
        roww = 0
        self.tableAdminEmployees_2.setRowCount(vehicleDL().vehicleCount)
        self.tableAdminEmployees_2.setColumnCount(8)
        # self.tableSaleAgentList.setHorizontalHeaderLabels(['Delete', 'Edit','Category', 'Brand', 'Model', 'Price' , 'Processor' , 'Resolution', 'Ram' , 'Storage' , 'Screen Size'])
        self.tableAdminEmployees_2.horizontalHeader().setVisible(True)
        stylesheet = "::section{Background-color:#48ACAC;color:white;}"
        self.tableAdminEmployees_2.horizontalHeader().setStyleSheet(stylesheet)
        self.tableAdminEmployees_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableAdminEmployees_2.setHorizontalHeaderLabels(['ID', 'Name', 'Brand', 'Category' , 'Capacity' , 'Number', 'Price', 'Date Entry'])
        start=vehicleDL().vehicleLinkedList.head
        if start is None:
            print("Empty List")
        else:
            while start:
                row=start.getProduct()
        
            # return (salesAgent.Id,salesAgent.login.role,salesAgent.login.userName,salesAgent.name,salesAgent.login.password,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
            # self.tableAdminEmployees.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableAdminEmployees_2.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.Id)))
                self.tableAdminEmployees_2.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.name)))
                self.tableAdminEmployees_2.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.brand)))
                self.tableAdminEmployees_2.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.category))))
                self.tableAdminEmployees_2.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.category)))
                self.tableAdminEmployees_2.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row.capacity)))
                self.tableAdminEmployees_2.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row.number)))
                self.tableAdminEmployees_2.setItem(roww, 7 , QtWidgets.QTableWidgetItem((str(row.dateCreated))  ))             
                roww = roww + 1
                start=start.getNextNode()
    def addVehicle(self):
        pass
        # self.newq=ManagerAddVehicle()
        # self.newq.show()
        # self.newq.btnAdd.clicked.connect(lambda:self.loadVehicleTable())
        # self.loadLabels()
        
    def editVehicle(self):
        if self.tableAdminEmployees_2.currentRow() != None and self.tableAdminEmployees_2.currentRow()>=0:
            row = self.tableAdminEmployees_2.currentRow()
            col = self.tableAdminEmployees_2.currentColumn()
            Id=self.tableAdminEmployees_2.item(row,0).text()
            name= self.tableAdminEmployees_2.item(row,1).text()
            brand = self.tableAdminEmployees_2.item(row,2).text()
            category = self.tableAdminEmployees_2.item(row,3).text()
            capacity = self.tableAdminEmployees_2.item(row,4).text()
            number = self.tableAdminEmployees_2.item(row,5).text()
            price = self.tableAdminEmployees_2.item(row,6).text()
            datePresent = self.tableAdminEmployees_2.item(row,7).text()
            v = vehicle(Id,name,brand,category ,capacity, number,price, datePresent) 
            # self.editVehicleWindow=ManagerEditVehicle(v)
            # self.editVehicleWindow.show()
            # self.loadSaleAgentData()
            # salesManDL().addAllSalesmanToFile()
            # self.editVehicleWindow.btnSave.clicked.connect(lambda:self.loadVehicleTable())
            # self.editVehicleWindow.btnSave.clicked.connect(lambda:vehicleDL().addAllVehicleToFile("VehicleInfo.csv"))
    def deleteVehicle(self):
        row = self.tableAdminEmployees_2.currentRow()
        print(row)
        if row>=0:
            qm =QMessageBox
            ret=qm.question(self,'', "Are you sure to delete this Vehicle?", qm.Yes | qm.No)           
            if ret==qm.Yes:
                row = self.tableAdminEmployees_2.currentRow()
                col = self.tableAdminEmployees_2.currentColumn()
                Id= self.tableAdminEmployees_2.item(row,0).text()
                name = self.tableAdminEmployees_2.item(row,1).text()
                brand = self.tableAdminEmployees_2.item(row,2).text()
                category = self.tableAdminEmployees_2.item(row,3).text()
                capacity = self.tableAdminEmployees_2.item(row,4).text()
                number = self.tableAdminEmployees_2.item(row,5).text()
                price = self.tableAdminEmployees_2.item(row,6).text()
                datePresent = self.tableAdminEmployees_2.item(row,7).text()       
                v = vehicle(Id,name,brand,category ,capacity, number,price, datePresent) 
                vehicleDL().deleteVehicle(v)
                self.loadVehicleTable()
                vehicleDL().addAllVehicleToFile(self.file_paths.VehicleInfo)   
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
    
    def loadLabels(self):
        
        count=str(deliveryManDL.deliveryManCount+orderDispatcherDL.oderDispactherCount+salesManDL.saleAgentCount+managerDL.managerCount)
        salaries=str(deliveryManDL().allDMSalaries()+orderDispatcherDL.allODSalaries()+salesManDL.allSaleAgentSalaries())
        self.lblAdminTotalInvProduct_3.setText(count)
        self.lblAdminTotalProduct_3.setText(count)
        self.lblAdminTotalProfit_3.setText(salaries)
        self.lblAdminTotalRevenue_3.setText(str(vehicleDL.vehicleCount))
