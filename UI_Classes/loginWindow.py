

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSizePolicy, QLabel, QProgressBar
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage, QIcon
from UI_Classes.loginWindow_ui import Ui_MainWindow  # Import the generated class
# from main import MainWindow  # Import the generated class
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.Credentials import credential
from DL.AdminDL import adminDL
from DL.OrderDispatcherDL import orderDispatcherDL
from DL.DeliveryManDL import deliveryManDL
from DL.VehicleDL import vehicleDL
from DL.SalesManDL import salesManDL
from DL.ManagerDL import managerDL
from DL.CategoryDL import categoryDL
from DL.ProductDL import productDL


# Get the current directory of the script
current_directory = os.path.dirname(__file__)

# Navigate one directory back to access the Data folder
data_directory = os.path.abspath(os.path.join(current_directory, os.pardir, "Data"))

# Define the file path
AdminInfo = os.path.join(data_directory, "AdminInfo.csv")
SalesManInfo = os.path.join(data_directory, "SalesManInfo.csv")
OrderDispatcherInfo = os.path.join(data_directory, "OrderDispatcherInfo.csv")
DeliveryManInfo = os.path.join(data_directory, "DeliveryManInfo.csv")

VehicleInfo = os.path.join(data_directory, "VehicleInfo.csv")
ProductsInfo = os.path.join(data_directory, "ProductsInfo.csv")
ManagerInfo = os.path.join(data_directory, "ManagerInfo.csv")
CategoriesList = os.path.join(data_directory, "CategoriesList.csv")

class LoginWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        # Set up the user interface from the generated class
        self.setupUi(self)
        # Set flags to remove the default title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.btnLogIn.clicked.connect(self.login)
        adminDL().loadAdminInfo(AdminInfo)
        salesManDL().loadSalesManInfo(SalesManInfo)
        orderDispatcherDL().loadODInfo(OrderDispatcherInfo)
        deliveryManDL().loaddeliveryManInfo(DeliveryManInfo)
        vehicleDL().loadVehicleInfo(VehicleInfo)
        productDL().loadProductsFromFile(ProductsInfo)
        managerDL().loadManagerInfo(ManagerInfo)
        categoryDL.readCategoryFromFile(CategoriesList)
        # managerDL.loadManagerInfo("ManagerInfo.csv")
    
    def login(self):
        userName = self.txtUserName.text()
        password = self.txtPassword.text()
        role = self.cmbRole.currentText()
        user = credential(userName, password, role)
        login = credential(userName, password, role)
        # if(role == "Admin"):
        #     # if(adminDL().searchAdmin(login)):
        #     self.newq = AdminWindow()
        #     self.newq.show()
        #         # self.newq.loadTableAdminEmployees(managerDL.managers)
        #         # self.newq.btnAdminDeleteEmployees.clicked.connect(lambda:self.newq.deleteUser())
                
                
        # elif(role == "Manager"):
        #     self.newq = ManagerWindow()
        #     self.newq.show()           
            
        # elif(role == "Sales Agent"):
        #     self.newq = SaleTeam()
        #     self.newq.show() 
        # elif(role == "Order Dispatcher"):
        #     self.OrderDispatcher = OrderDispatcher()
        #     self.OrderDispatcher.show()
        # elif(role == "Delivery Man"):
        #     print("Delivery Man")