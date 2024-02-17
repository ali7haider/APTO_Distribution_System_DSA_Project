# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:34:26 2024

@author: Digital Zone
"""


import os
from PyQt5.QtWidgets import QMainWindow
from UI_Classes.orderDispatcherWindow_ui import Ui_MainWindow
from BL.file_paths import FilePaths

class OrderDispatcherWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(OrderDispatcherWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
        self.stackedWidget.setCurrentWidget(self.OrderDispatcherDashBoard)
        self.btnOrderDispatcherDashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.OrderDispatcherDashBoard))
        self.btnOrderDispatcherAccount.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AccountDetails))
        self.btnOrderDispatcherNewOrders.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.OrderDispatcherNewOrders))
        self.btnOrderDispatcherLogOut.clicked.connect(lambda:self.close());
