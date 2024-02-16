# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 00:01:18 2024

@author: Digital Zone
"""

from PyQt5.QtWidgets import QApplication

from UI_Classes.loginWindow import LoginWindow
import sys
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())