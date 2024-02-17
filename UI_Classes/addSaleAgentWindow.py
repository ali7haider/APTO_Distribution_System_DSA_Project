# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:42:37 2024

@author: Digital Zone
"""
import os
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from UI_Classes.orderDispatcher_ui import Ui_MainWindow
from DL.SalesManDL import salesManDL
from BL.file_paths import FilePaths
from BL.SalesMan import salesMan
from datetime import date
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore, QtGui

class AddSaleAgentWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AddSaleAgentWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
        self.btnAdd.clicked.connect(self.saveNewSaleAgentData)
        self.btnCancel.clicked.connect(lambda: self.close())
        self.implementingValidation()
        self.dateEditAddAgent.setDate(date.today())
        
    def implementingValidation(self):
        rx  = QtCore.QRegExp("[0-9]{13}")   
        val = QtGui.QRegExpValidator(rx)
        self.txtCNIC.setValidator(val)
        # self.txtCNIC.setMaxLength(17)
        self.txtSalary.setValidator(QIntValidator())
        self.txtCellNo.setInputMask("+99_999_9999999")
        self.txtID.setInputMask("S_999999")
    def ValidationChecker(self,Id,name,cnic,email,userName,password,cellNo,salary,vehicle,dateCreated):
        flag=True
        if Id=="S_":            
            self.lblIDValidation.setText("*Enter ID of Sale Agent ""SA_num"" ")
            flag=False
        else:
            self.lblIDValidation.setText("")        
        if name=="":
            self.lblNameValidation.setText("*Enter Name of Sale Agent")
            flag=False
        else:
            self.lblNameValidation.setText("")
        if cnic=="" or len(cnic)!=13:
            self.lblCNICValidation.setText("*Enter 13 Digits CNIC Without Dashes")
        else:
            self.lblCNICValidation.setText("")
        if email=="":
            self.lblEmailValidation.setText("*Enter Correct form of Email ""*****@gmail.com"" ")
            flag=False
        else:
            self.lblEmailValidation.setText("")
        if userName=="":
            self.lblUserNameValidation.setText("*Enter User Name")
            flag=False
        else:
            self.lblUserNameValidation.setText("")
        if password=="":
            self.lblPasswordValidation.setText("*Enter Minimum of 8 character")
            flag=False
        else:
            self.lblPasswordValidation.setText("")
        if cellNo=="" or len(cellNo)!=15:
            self.txtCellNoValidation.setText("*Enter in correct form +92_323_XXXXXXX")
            flag=False
        else:
            self.txtCellNoValidation.setText("")
        if salary=="":
            self.lblSalaryValidation.setText("*Enter Salary")
            flag=False
        else:
            self.lblSalaryValidation.setText("")
            
        if vehicle=="Select":
            self.lblVehicleValidation.setText("*Select Vehicle")
            flag=False
        else:
            self.lblVehicleValidation.setText("")
           
        today=date.today()
        dateToday=today.strftime("20%y-%m-%d")
        # if dateCreated<dateToday:
        #     self.lblDateValidation.setText("*Date should be of Today or Greater")
        #     flag=False
        # else:
        #     self.lblDateValidation.setText("")
        if flag==True:
            return True
        else:
            return False
            
    def saveNewSaleAgentData(self):  
        Id = self.txtID.text()
        name = self.txtName.text()
        cnic = self.txtCNIC.text()
        email = self.txtEmail.text()
        userName = self.txtUserName.text()
        password = str(self.txtPassword.text())
        cellNo = self.txtCellNo.text()
        vehicle = self.cmbxVehicle.currentText()
        dateCreated = self.dateEditAddAgent.date()
        today=date.today()
        dateCreated = self.dateEditAddAgent.date().toPyDate()
        role="Sales Agent"
        salary = self.txtSalary.text()
        if self.ValidationChecker(Id,name,cnic,email,userName,password,cellNo,salary,vehicle,dateCreated):
            salesAgent = salesMan(userName, password,role, name, cnic, email, cellNo, Id, dateCreated, vehicle, salary)
            # print(salesAgent.Id,salesAgent.login.userName,salesAgent.login.password,salesAgent.login.role,salesAgent.cnic,salesAgent.email,salesAgent.cellNo,salesAgent.dateCreated,salesAgent.vehicle,salesAgent.salary)
            # print(salesAgent.login.password)
            salesManDL().addSalesMan(salesAgent)
            salesManDL().addSalesmanToFile(self.file_paths.SalesManInfo,salesAgent)
            msg = QMessageBox()
            msg.setText("Done")
            msg.setInformativeText('User Added Succesfully')
            msg.setWindowTitle("Successful")
            msg.exec_()
            self.close()
            # self.loadSaleAgentData()