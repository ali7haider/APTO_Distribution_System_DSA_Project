import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from UI_Classes.loginWindow_ui import Ui_MainWindow
from BL.Credentials import credential
from DL.AdminDL import adminDL
from DL.OrderDispatcherDL import orderDispatcherDL
from DL.DeliveryManDL import deliveryManDL
from DL.VehicleDL import vehicleDL
from DL.SalesManDL import salesManDL
from DL.ManagerDL import managerDL
from DL.CategoryDL import categoryDL
from DL.ProductDL import productDL
from BL.file_paths import FilePaths
from UI_Classes.adminWindow import AdminWindow
from UI_Classes.managerWindow import ManagerWindow

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        # Set up the user interface from the generated class
        self.setupUi(self)
        # Set flags to remove the default title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.btnLogIn.clicked.connect(self.login)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))
        self.load_data()
        # Connect the closeAppBtn button to the close method
        self.btnClose.clicked.connect(self.close)
    def load_data(self):
        adminDL().loadAdminInfo(self.file_paths.AdminInfo)
        salesManDL().loadSalesManInfo(self.file_paths.SalesManInfo)
        orderDispatcherDL().loadODInfo(self.file_paths.OrderDispatcherInfo)
        deliveryManDL().loaddeliveryManInfo(self.file_paths.DeliveryManInfo)
        vehicleDL().loadVehicleInfo(self.file_paths.VehicleInfo)
        productDL().loadProductsFromFile(self.file_paths.ProductsInfo)
        managerDL().loadManagerInfo(self.file_paths.ManagerInfo)
        categoryDL.readCategoryFromFile(self.file_paths.CategoriesList)

    def login(self):
        userName = self.txtUserName.text()
        password = self.txtPassword.text()
        role = self.cmbRole.currentText()
        user = credential(userName, password, role)
        login = credential(userName, password, role)
        if(role == "Admin"):
            # if(adminDL().searchAdmin(login)):
            self.newq = AdminWindow()
            self.newq.show()
        if(role == "Manager"):
            # if(adminDL().searchAdmin(login)):
            self.newq = ManagerWindow()
            self.newq.show()