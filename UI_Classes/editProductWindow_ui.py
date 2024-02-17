# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addProductWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 700)
        MainWindow.setMinimumSize(QtCore.QSize(600, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.headerLabel = QtWidgets.QLabel(self.frame_2)
        self.headerLabel.setGeometry(QtCore.QRect(1, 5, 570, 50))
        self.headerLabel.setMinimumSize(QtCore.QSize(570, 50))
        self.headerLabel.setMaximumSize(QtCore.QSize(570, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.headerLabel.setFont(font)
        self.headerLabel.setStyleSheet("color:#48ACAC")
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 100))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_21 = QtWidgets.QFrame(self.frame_3)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 40)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_25 = QtWidgets.QFrame(self.frame_21)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_79 = QtWidgets.QLabel(self.frame_25)
        self.label_79.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("color:#48ACAC")
        self.label_79.setObjectName("label_79")
        self.verticalLayout_3.addWidget(self.label_79)
        self.frame_13 = QtWidgets.QFrame(self.frame_25)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.txtID = QtWidgets.QLineEdit(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtID.setFont(font)
        self.txtID.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtID.setPlaceholderText("")
        self.txtID.setObjectName("txtID")
        self.verticalLayout_14.addWidget(self.txtID)
        self.lblIdError = QtWidgets.QLabel(self.frame_13)
        self.lblIdError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblIdError.setText("")
        self.lblIdError.setObjectName("lblIdError")
        self.verticalLayout_14.addWidget(self.lblIdError)
        self.verticalLayout_3.addWidget(self.frame_13)
        self.verticalLayout_22.addWidget(self.frame_25)
        self.frame_26 = QtWidgets.QFrame(self.frame_21)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_24.addItem(spacerItem1)
        self.label_80 = QtWidgets.QLabel(self.frame_26)
        self.label_80.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("color:#48ACAC")
        self.label_80.setObjectName("label_80")
        self.verticalLayout_24.addWidget(self.label_80)
        self.frame_28 = QtWidgets.QFrame(self.frame_26)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.txtQuantity = QtWidgets.QLineEdit(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtQuantity.setFont(font)
        self.txtQuantity.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtQuantity.setObjectName("txtQuantity")
        self.verticalLayout_26.addWidget(self.txtQuantity)
        self.lblQuantityError = QtWidgets.QLabel(self.frame_28)
        self.lblQuantityError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblQuantityError.setText("")
        self.lblQuantityError.setObjectName("lblQuantityError")
        self.verticalLayout_26.addWidget(self.lblQuantityError)
        self.verticalLayout_24.addWidget(self.frame_28)
        self.verticalLayout_22.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.frame_21)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_25.addItem(spacerItem2)
        self.label_81 = QtWidgets.QLabel(self.frame_27)
        self.label_81.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color:#48ACAC")
        self.label_81.setObjectName("label_81")
        self.verticalLayout_25.addWidget(self.label_81)
        self.frame_29 = QtWidgets.QFrame(self.frame_27)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.txtSalesPrice = QtWidgets.QLineEdit(self.frame_29)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtSalesPrice.setFont(font)
        self.txtSalesPrice.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtSalesPrice.setObjectName("txtSalesPrice")
        self.verticalLayout_27.addWidget(self.txtSalesPrice)
        self.lblSalesPriceError = QtWidgets.QLabel(self.frame_29)
        self.lblSalesPriceError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblSalesPriceError.setText("")
        self.lblSalesPriceError.setObjectName("lblSalesPriceError")
        self.verticalLayout_27.addWidget(self.lblSalesPriceError)
        self.verticalLayout_25.addWidget(self.frame_29)
        self.verticalLayout_22.addWidget(self.frame_27)
        self.horizontalLayout.addWidget(self.frame_21)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 40)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.frame_6)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_11.addItem(spacerItem3)
        self.label_83 = QtWidgets.QLabel(self.frame_14)
        self.label_83.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setStyleSheet("color:#48ACAC")
        self.label_83.setObjectName("label_83")
        self.verticalLayout_11.addWidget(self.label_83)
        self.frame_30 = QtWidgets.QFrame(self.frame_14)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.txtName = QtWidgets.QLineEdit(self.frame_30)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtName.setFont(font)
        self.txtName.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtName.setObjectName("txtName")
        self.verticalLayout_28.addWidget(self.txtName)
        self.lblNameError = QtWidgets.QLabel(self.frame_30)
        self.lblNameError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblNameError.setText("")
        self.lblNameError.setObjectName("lblNameError")
        self.verticalLayout_28.addWidget(self.lblNameError)
        self.verticalLayout_11.addWidget(self.frame_30)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_6)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_12.addItem(spacerItem4)
        self.label_84 = QtWidgets.QLabel(self.frame_15)
        self.label_84.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setStyleSheet("color:#48ACAC")
        self.label_84.setObjectName("label_84")
        self.verticalLayout_12.addWidget(self.label_84)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.txtDescription = QtWidgets.QLineEdit(self.frame_17)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtDescription.setFont(font)
        self.txtDescription.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtDescription.setObjectName("txtDescription")
        self.verticalLayout_17.addWidget(self.txtDescription)
        self.lblDescriptionError = QtWidgets.QLabel(self.frame_17)
        self.lblDescriptionError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblDescriptionError.setText("")
        self.lblDescriptionError.setObjectName("lblDescriptionError")
        self.verticalLayout_17.addWidget(self.lblDescriptionError)
        self.verticalLayout_12.addWidget(self.frame_17)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_6)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem5 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_13.addItem(spacerItem5)
        self.label_85 = QtWidgets.QLabel(self.frame_16)
        self.label_85.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_85.setFont(font)
        self.label_85.setStyleSheet("color:#48ACAC")
        self.label_85.setObjectName("label_85")
        self.verticalLayout_13.addWidget(self.label_85)
        self.frame_22 = QtWidgets.QFrame(self.frame_16)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.expiryDate = QtWidgets.QDateEdit(self.frame_22)
        self.expiryDate.setMinimumSize(QtCore.QSize(0, 25))
        self.expiryDate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.expiryDate.setObjectName("expiryDate")
        self.verticalLayout_18.addWidget(self.expiryDate)
        self.lblExpiryError = QtWidgets.QLabel(self.frame_22)
        self.lblExpiryError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblExpiryError.setText("")
        self.lblExpiryError.setObjectName("lblExpiryError")
        self.verticalLayout_18.addWidget(self.lblExpiryError)
        self.verticalLayout_13.addWidget(self.frame_22)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 40)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_18 = QtWidgets.QFrame(self.frame_7)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_15.addItem(spacerItem6)
        self.label_87 = QtWidgets.QLabel(self.frame_18)
        self.label_87.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setStyleSheet("color:#48ACAC")
        self.label_87.setObjectName("label_87")
        self.verticalLayout_15.addWidget(self.label_87)
        self.frame_23 = QtWidgets.QFrame(self.frame_18)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.cmbCategory = QtWidgets.QComboBox(self.frame_23)
        self.cmbCategory.setMinimumSize(QtCore.QSize(0, 25))
        self.cmbCategory.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cmbCategory.setStyleSheet("border:1px solid grey;")
        self.cmbCategory.setObjectName("cmbCategory")
        self.cmbCategory.addItem("")
        self.cmbCategory.addItem("")
        self.cmbCategory.addItem("")
        self.cmbCategory.addItem("")
        self.cmbCategory.addItem("")
        self.verticalLayout_19.addWidget(self.cmbCategory)
        self.lblCategoryError = QtWidgets.QLabel(self.frame_23)
        self.lblCategoryError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblCategoryError.setText("")
        self.lblCategoryError.setObjectName("lblCategoryError")
        self.verticalLayout_19.addWidget(self.lblCategoryError)
        self.verticalLayout_15.addWidget(self.frame_23)
        self.verticalLayout_6.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_7)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_16.addItem(spacerItem7)
        self.label_88 = QtWidgets.QLabel(self.frame_19)
        self.label_88.setMaximumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("color:#48ACAC")
        self.label_88.setObjectName("label_88")
        self.verticalLayout_16.addWidget(self.label_88)
        self.frame_24 = QtWidgets.QFrame(self.frame_19)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.txtProductionCost = QtWidgets.QLineEdit(self.frame_24)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtProductionCost.setFont(font)
        self.txtProductionCost.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtProductionCost.setObjectName("txtProductionCost")
        self.verticalLayout_20.addWidget(self.txtProductionCost)
        self.lblProductionError = QtWidgets.QLabel(self.frame_24)
        self.lblProductionError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblProductionError.setText("")
        self.lblProductionError.setObjectName("lblProductionError")
        self.verticalLayout_20.addWidget(self.lblProductionError)
        self.verticalLayout_16.addWidget(self.frame_24)
        self.verticalLayout_6.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_7)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem8 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_10.addItem(spacerItem8)
        self.label_86 = QtWidgets.QLabel(self.frame_20)
        self.label_86.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setStyleSheet("color:#48ACAC")
        self.label_86.setObjectName("label_86")
        self.verticalLayout_10.addWidget(self.label_86)
        self.frame_31 = QtWidgets.QFrame(self.frame_20)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.dateAdded = QtWidgets.QDateEdit(self.frame_31)
        self.dateAdded.setMinimumSize(QtCore.QSize(0, 25))
        self.dateAdded.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dateAdded.setObjectName("dateAdded")
        self.verticalLayout_21.addWidget(self.dateAdded)
        self.lblDateError = QtWidgets.QLabel(self.frame_31)
        self.lblDateError.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblDateError.setText("")
        self.lblDateError.setObjectName("lblDateError")
        self.verticalLayout_21.addWidget(self.lblDateError)
        self.verticalLayout_10.addWidget(self.frame_31)
        self.verticalLayout_6.addWidget(self.frame_20)
        self.horizontalLayout.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 100))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.btnCancel = QtWidgets.QPushButton(self.frame_8)
        self.btnCancel.setMinimumSize(QtCore.QSize(0, 35))
        self.btnCancel.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet("#btnCancel\n"
"{\n"
"\n"
"background-color: #986262;\n"
"color: white;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"#btnCancel::hover\n"
"{\n"
"background-color:#AE4D4D;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.btnAdd = QtWidgets.QPushButton(self.frame_8)
        self.btnAdd.setMinimumSize(QtCore.QSize(0, 35))
        self.btnAdd.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.btnAdd.setFont(font)
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("\n"
"#btnAdd\n"
"{\n"
"border-radius:10px;\n"
"background-color: #48ACAC;\n"
"color:white;\n"
"}\n"
"#btnAdd::hover\n"
"{\n"
"background-color:#2F958D;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_3.addWidget(self.btnAdd)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headerLabel.setText(_translate("MainWindow", "Products   >>  Add New Product"))
        self.label_79.setText(_translate("MainWindow", "ID"))
        self.label_80.setText(_translate("MainWindow", "Quantity"))
        self.txtQuantity.setPlaceholderText(_translate("MainWindow", "Enter Quantity of Product"))
        self.label_81.setText(_translate("MainWindow", "Sales Price"))
        self.txtSalesPrice.setPlaceholderText(_translate("MainWindow", "Enter Sales Price of Product"))
        self.label_83.setText(_translate("MainWindow", "Name"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "Enter Name of Product"))
        self.label_84.setText(_translate("MainWindow", "Description"))
        self.txtDescription.setPlaceholderText(_translate("MainWindow", "Enter Description of Product"))
        self.label_85.setText(_translate("MainWindow", "Expiry Date"))
        self.label_87.setText(_translate("MainWindow", "Category"))
        self.cmbCategory.setItemText(0, _translate("MainWindow", "Juices & Food Drinks"))
        self.cmbCategory.setItemText(1, _translate("MainWindow", "Nestle Water"))
        self.cmbCategory.setItemText(2, _translate("MainWindow", "Coffee"))
        self.cmbCategory.setItemText(3, _translate("MainWindow", "Breakfast Cereals"))
        self.cmbCategory.setItemText(4, _translate("MainWindow", "Infant Nutrition"))
        self.label_88.setText(_translate("MainWindow", "Production Cost"))
        self.txtProductionCost.setPlaceholderText(_translate("MainWindow", "Enter Production Cost"))
        self.label_86.setText(_translate("MainWindow", "Date"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
import UI_Classes.resources_rc
