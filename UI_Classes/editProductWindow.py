# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:06:01 2024

@author: Digital Zone
"""

import os
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from UI_Classes.editProductWindow_ui import Ui_MainWindow
from DL.ProductDL import productDL
from BL.file_paths import FilePaths
from BL.Product import product
from datetime import date
from PyQt5.QtGui import QIntValidator
from datetime import datetime
class EditProductWindow(QMainWindow,Ui_MainWindow):
    def __init__(self , p):
        super(EditProductWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
        self.implementingValidation()
        self.btnCancel.clicked.connect(lambda : self.close())
        self.btnAdd.clicked.connect(lambda : self.editProduct(p))
        self.dateAdded.setDate(date.today())
        self.txtID.setEnabled(False)
        self.fillInformation(p)
        self.headerLabel.setText("Products   >>  Edit Product")
        self.btnAdd.setText("Edit")
        
    def implementingValidation(self):
        self.txtID.setInputMask("P_999999")
        self.txtQuantity.setValidator(QIntValidator())
        self.txtProductionCost.setValidator(QIntValidator())
        self.txtSalesPrice.setValidator(QIntValidator())
    def fillInformation(self, p):
        
        self.txtID.setText(p.Id)
        self.txtName.setText(p.name)
        self.cmbCategory.setCurrentText(p.category)
        self.txtQuantity.setText(p.quantity)
        self.txtDescription.setText(p.description)
        self.txtProductionCost.setText(p.productionCost)
        self.txtSalesPrice.setText(p.salePrice)
        expiryDate = datetime.strptime(p.expiryDate, '%d/%m/%Y').date()
        self.expiryDate.setDate(expiryDate)
        date = datetime.strptime(p.date, '%d/%m/%Y').date()
        self.dateAdded.setDate(date)
        
    def editProduct(self,p):
        flag = True;
        ID = self.txtID.text()
        name = self.txtName.text()
        category = self.cmbCategory.currentText()
        quantity = self.txtQuantity.text()
        description = self.txtDescription.text()
        productionCost = self.txtProductionCost.text()
        salesPrice = self.txtSalesPrice.text()
        expiryDate = self.expiryDate.text()
        date = self.dateAdded.text()
        if(ID == "P_"):
            self.lblIdError.setText("*This Field is Required")
            flag = False
        else:
            self.lblIdError.setText("")
        if(quantity == "" or quantity == "0"):
            self.lblQuantityError.setText("*This Field is Required")
            flag = False
        else:
            self.lblQuantityError.setText("")
        if(name == ""):
            self.lblNameError.setText("*This Field is Required")
            flag = False
        else:
            self.lblNameError.setText("")
        if(productionCost == "" or productionCost == "0"):
            self.lblProductionError.setText("*This Field is Required")
            flag = False
        else:
            self.lblProductionError.setText("")
        if(description == ""):
            self.lblDescriptionError.setText("*This Field is Required")
            flag = False
        else:
            self.lblDescriptionError.setText("")
        if(salesPrice == "" or salesPrice == "0"):
            self.lblSalesPriceError.setText("*This Field is Required")
            flag = False
        else:
            self.lblSalesPriceError.setText("")
        if(expiryDate <= date):
            self.lblExpiryError.setText("*Invalid Expiry Date")
            flag = False
        elif(self.lblExpiryError.text() == "*Invalid Expiry Date"):
            self.lblExpiryError.setText("")
        if(productionCost != "" and salesPrice != ""):
            if(int(productionCost) >= int(salesPrice)):
                self.lblSalesPriceError.setText("*Sales Price Should be Greater than Production Cost")
                flag = False
            elif(self.lblExpiryError.text() == "*Sales Price Should be Greater than Production Cost"):
                self.lblExpiryError.setText("")

        if(flag == True):
            u = product(name, ID, category, quantity, description, productionCost, salesPrice, date, expiryDate)
            productDL().editProduct(p, u)
            productDL().storeAllProductInFile("ProductsInfo.csv")
            msg = QMessageBox()
            msg.setText("Done")
            msg.setInformativeText('Product Edited Successfully!')
            msg.setWindowTitle("Edited")
            msg.exec_()