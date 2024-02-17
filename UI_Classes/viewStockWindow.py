# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:12:25 2024

@author: Digital Zone
"""


import os
from PyQt5.QtWidgets import QMainWindow
from UI_Classes.viewStockWindow_ui import Ui_MainWindow
from DL.ProductDL import productDL
from BL.file_paths import FilePaths
from PyQt5 import QtCore,QtWidgets
class ViewStockWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
       super(ViewStockWindow,self).__init__()
       self.setupUi(self)
       self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
       self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
       self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
       self.populateAllStock()
       self.btnSaleTeamViewStockClose.clicked.connect(lambda: self.close())
    def populateAllStock(self):
        roww = 0
        self.tableSaleTeamViewStock.setRowCount(len(productDL.AllProducts))
        self.tableSaleTeamViewStock.setColumnCount(8)
        self.tableSaleTeamViewStock.setHorizontalHeaderLabels(['Product Name', 'Product ID','Category',
                                                               'Quantity','Description','Production Cost',
                                                               'Sale Price','Date Added'])
       
        self.tableSaleTeamViewStock.horizontalHeader().setVisible(True)
        stylesheet = "::section{Background-color:#48ACAC;color:white;}"
        self.tableSaleTeamViewStock.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.tableSaleTeamViewStock.horizontalHeader().setStyleSheet(stylesheet)
        for i in range(len(productDL.AllProducts)):
            row = productDL.AllProducts[i]
            self.tableSaleTeamViewStock.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row.name)))
            self.tableSaleTeamViewStock.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row.ID)))
            self.tableSaleTeamViewStock.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row.category)))
            self.tableSaleTeamViewStock.setItem(roww, 3 , QtWidgets.QTableWidgetItem((str(row.quantity))))
            self.tableSaleTeamViewStock.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row.description)))
            self.tableSaleTeamViewStock.setItem(roww, 5 , QtWidgets.QTableWidgetItem((str(row.productionCost))))
            self.tableSaleTeamViewStock.setItem(roww, 6 , QtWidgets.QTableWidgetItem((str(row.salesPrice))))
            self.tableSaleTeamViewStock.setItem(roww, 7 , QtWidgets.QTableWidgetItem((str(row.date ))))
            roww = roww + 1
 