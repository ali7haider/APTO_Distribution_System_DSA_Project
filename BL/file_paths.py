# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 01:00:31 2024

@author: Digital Zone
"""

import os

class FilePaths:
    def __init__(self, data_directory):
        self.data_directory = data_directory
        self.AdminInfo = os.path.join(data_directory, "AdminInfo.csv")
        self.SalesManInfo = os.path.join(data_directory, "SalesManInfo.csv")
        self.OrderDispatcherInfo = os.path.join(data_directory, "OrderDispatcherInfo.csv")
        self.DeliveryManInfo = os.path.join(data_directory, "DeliveryManInfo.csv")
        self.VehicleInfo = os.path.join(data_directory, "VehicleInfo.csv")
        self.ProductsInfo = os.path.join(data_directory, "ProductsInfo.csv")
        self.ManagerInfo = os.path.join(data_directory, "ManagerInfo.csv")
        self.CategoriesList = os.path.join(data_directory, "CategoriesList.csv")
