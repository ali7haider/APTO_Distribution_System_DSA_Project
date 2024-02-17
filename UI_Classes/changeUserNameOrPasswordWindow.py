# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:23:16 2024

@author: Digital Zone
"""
import os
from PyQt5.QtWidgets import QMainWindow
from UI_Classes.changeUserNameOrPasswordWindow_ui import Ui_MainWindow
from BL.file_paths import FilePaths
class ChangeUserNameOrPasswordWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(ChangeUserNameOrPasswordWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
        self.btnCancel.clicked.connect(lambda:self.close())
        self.btnAdd.clicked.connect(lambda:self.saveCredentials())
    def saveCredentials(self):
        userName=self.txtUserName.text()
        password=self.txtPassword.text()
        print(userName,password)
        self.close()
        