# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:28:59 2024

@author: Digital Zone
"""
import os
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from UI_Classes.editVehicleWindow_ui import Ui_MainWindow
from DL.VehicleDL import vehicleDL
from BL.file_paths import FilePaths
from BL.Vehicle import vehicle
from datetime import date
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore, QtGui
from datetime import datetime
class AddVehicleWindow(QMainWindow):
    def __init__(self):
        super(AddVehicleWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
      
        self.btnAdd.clicked.connect(self.saveNewVehicleData)
        self.btnCancel.clicked.connect(lambda: self.close())
        self.implementingValidation()
        self.dateAddOrderDispatcher.setDate(date.today())
    def implementingValidation(self):
        # self.txtCNIC.setMaxLength(17)
        self.txtPrice.setValidator(QIntValidator())
        self.txtID.setInputMask("V_999999")
    def saveNewVehicleData(self):
        Id = self.txtID.text()
        name = self.txtName.text()
        brand = self.txtBrand.text()
        category = self.txtCategory.text()
        capacity = self.txtCapacity.text()
        number = str(self.txtNumber.text())
        price = self.txtPrice.text()
        dateCreated = self.dateAddOrderDispatcher.date().toPyDate()
        today=date.today()
        if self.ValidationChecker(Id,name,brand,category,capacity,number,price,dateCreated):
            v = vehicle(Id,name,brand,category ,capacity, number,price, dateCreated)   
            # print(salesAgent.Id,salesAgent.login.userName,salesAgent.login.password,salesAgent.login.role,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
            # print(salesAgent.login.password)
            vehicleDL().addVehicle(v)
            vehicleDL().addVehicleToFile(self.file_paths.VehicleInfo,v)
            msg = QMessageBox()
            msg.setText("Done")
            msg.setInformativeText('Vehicle Added Succesfully')
            msg.setWindowTitle("Successful")
            msg.exec_()
            self.close()
    def ValidationChecker(self,Id,name,brand,category,capacity,number,price,dateCreated):
        flag=True
        if Id=="V_":            
            self.lblIDValidation.setText("*Enter ID")
            flag=False
        else:
            self.lblIDValidation.setText("")        
        if name=="":
            self.lblNameValidation.setText("*Enter Name")
            flag=False
        else:
            self.lblNameValidation.setText("")
        if brand=="" :
            self.lblBrandValidation.setText("*Enter Brand")
        else:
            self.lblBrandValidation.setText("")
        if category=="":
            self.lblCategory.setText("*Enter Category")
            flag=False
        else:
            self.lblCategory.setText("")
        if capacity=="":
            self.lblCapacityValidation.setText("*Enter Capacity")
            flag=False
        else:
            self.lblCapacityValidation.setText("")
        if number=="":
            self.lblNumberValidation.setText("*Enter Number")
            flag=False
        else:
            self.lblNumberValidation.setText("")
        if price=="":
            self.lblPriceValidation.setText("*Enter Price")
            flag=False
        else:
            self.lblPriceValidation.setText("")
           
        # today=date.today()
        # dateToday=today.strftime("20%y-%m-%d")
        # if dateCreated<dateToday:
        #     self.lblDateValidation.setText("*Date should be of Today or Greater")
        #     flag=False
        # else:
        #     self.lblDateValidation.setText("")
        if flag==True:
            return True
        else:
            return False