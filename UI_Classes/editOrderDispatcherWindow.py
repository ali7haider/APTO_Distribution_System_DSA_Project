# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:41:58 2024

@author: Digital Zone
"""
import os
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from UI_Classes.editOrderDispatcherWindow_ui import Ui_MainWindow
from DL.OrderDispatcherDL import orderDispatcherDL
from BL.file_paths import FilePaths
from BL.OrderDispatcher import orderDispatcher
from datetime import date
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore, QtGui
from datetime import datetime
class EditOrderDispatcherWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,S):
        super(EditOrderDispatcherWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))      
        self.txtID.setEnabled(False)
        self.implementingValidation()  
        self.fillInformation(S)
        
        # self.btnAdd.clicked.connect(self.saveNewSaleAgentData)
        self.btnSave.clicked.connect(lambda:self.saveODData(S))
        self.btnCancel.clicked.connect(lambda: self.close())
    
    def fillInformation(self,S):
        self.txtID.setEnabled(False)
        self.txtID.setText(S.Id)
        self.txtName.setText(S.name)
        self.txtCNIC.setText(S.cnic)
        self.txtEmail.setText(S.email)
        self.txtUserName.setText(S.login.userName)
        self.txtPassword.setText(S.login.password)
        self.txtCellNo.setText(S.cellNo)
        self.txtSalary.setText(S.salary)
        expiryDate = datetime.strptime(S.dateCreated, '20%y-%m-%d').date()
        self.dateEditAddAgent_2.setDate(expiryDate)
        
    def implementingValidation(self):
        rx  = QtCore.QRegExp("[0-9]{13}")   
        val = QtGui.QRegExpValidator(rx)
        self.txtCNIC.setValidator(val)
        # self.txtCNIC.setMaxLength(17)
        self.txtSalary.setValidator(QIntValidator())
        self.txtCellNo.setInputMask("+99_999_9999999")
        self.txtID.setInputMask("O_999999")
    def ValidationChecker(self,Id,name,cnic,email,userName,password,cellNo,salary,dateCreated):
        flag=True
        if Id=="O_":            
            self.lblIDValidation.setText("*Enter ID ")
            flag=False
        else:
            self.lblIDValidation.setText("")        
        if name=="":
            self.lblNameValidation.setText("*Enter Name")
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
        today=date.today()
        dateToday=today.strftime("20%y-%m-%d")
        if dateCreated<dateToday:
            self.lblDateValidation_2.setText("*Date should be of Today or Greater")
            flag=False
        else:
            self.lblDateValidation_2.setText("")
        if flag==True:
            return True
        else:
            return False
    def saveODData(self,previous):
        Id = str(self.txtID.text())
        name = str(self.txtName.text())
        cnic = self.txtCNIC.text()
        email = str(self.txtEmail.text())
        userName = str(self.txtUserName.text())
        password = str(self.txtPassword.text())
        cellNo = str(self.txtCellNo.text())
        dateCreated = self.dateEditAddAgent_2.date().toPyDate()
        role="Order Dispatcher"
        salary = self.txtSalary.text()
        if self.ValidationChecker(Id,name,cnic,email,userName,password,cellNo,salary,dateCreated):
            new = orderDispatcher(userName, password,role, name, cnic, email, cellNo, Id, dateCreated,salary)
            orderDispatcherDL().EditODDataToList(previous,new)
            # salesManDL().addSalesmanToFile(salesAgent)
            msg = QMessageBox()
            msg.setText("Done")
            msg.setInformativeText('User Data Updated Succesfully')
            msg.setWindowTitle("Successful")
            msg.exec_()
            self.close()