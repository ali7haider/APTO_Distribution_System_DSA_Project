# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:02:31 2024

@author: Digital Zone
"""

import os
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from UI_Classes.addManagerWindow_ui import Ui_MainWindow
from DL.ManagerDL import managerDL
from BL.file_paths import FilePaths
from BL.Manager import manager
from datetime import date
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore, QtGui

class AddManagerWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AddManagerWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
        self.btnCancel.clicked.connect(lambda : self.close())
        self.btnAdd.clicked.connect(lambda : self.addManager())
        self.dateEditAddAgent.setDate(date.today())
        self.implementingValidation()
    def implementingValidation(self):
        rx  = QtCore.QRegExp("[0-9]{13}")   
        val = QtGui.QRegExpValidator(rx)
        self.txtCNIC.setValidator(val)
        # self.txtCNIC.setMaxLength(17)
        self.txtSalary.setValidator(QIntValidator())
        self.txtCellNo.setInputMask("+99_999_9999999")
        self.txtID.setInputMask("M_999999")
    
    def addManager(self):
        flag = True;
        Id = self.txtID.text()
        role="Manager"
        name = self.txtName.text()
        cnic = self.txtCNIC.text()
        email = self.txtEmail.text()
        userName = self.txtUserName.text()
        password = self.txtPassword.text()
        cellNo = self.txtCellNo.text()
        salary = self.txtSalary.text()
        dateCreated = self.dateEditAddAgent.date().toPyDate()
        if Id=="M_":            
            self.lblIDValidation.setText("*Enter ID  ")
            flag=False
        else:
            self.lblIDValidation.setText("")        
        if name=="":
            self.lblNameValidation.setText("*Enter Name ")
            flag=False
        else:
            self.lblNameValidation.setText("")
        if cnic=="" or len(cnic)!=13:
            self.lblCNICValidation.setText("*Enter 13 Digits CNIC Without Dashes")
            flag=False
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
            

        if(flag == True):
            if managerDL().managers.checkID(Id)==True:
                p = manager(userName, password, role, name, cnic, email, cellNo, Id, dateCreated, salary)
                managerDL().addManager(p)
                managerDL().addManagerToFile(self.file_paths.ManagerInfo, p)
                msg = QMessageBox()
                msg.setText("Done")
                msg.setInformativeText('User Added Successfully!')
                msg.setWindowTitle("Added")
                msg.exec_()            
                self.close()
            else:
                self.lblIDValidation.setText("ID Already Exist ")  