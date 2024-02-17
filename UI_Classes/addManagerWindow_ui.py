# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addManagerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_65 = QtWidgets.QLabel(self.frame_2)
        self.label_65.setMinimumSize(QtCore.QSize(570, 50))
        self.label_65.setMaximumSize(QtCore.QSize(570, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("color:#48ACAC")
        self.label_65.setObjectName("label_65")
        self.verticalLayout_3.addWidget(self.label_65)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 420))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 40)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_79 = QtWidgets.QLabel(self.frame_10)
        self.label_79.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("color:#48ACAC")
        self.label_79.setObjectName("label_79")
        self.verticalLayout_7.addWidget(self.label_79)
        self.frame_22 = QtWidgets.QFrame(self.frame_10)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_19.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_19.setSpacing(1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.txtID = QtWidgets.QLineEdit(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtID.setFont(font)
        self.txtID.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtID.setObjectName("txtID")
        self.verticalLayout_19.addWidget(self.txtID)
        self.lblIDValidation = QtWidgets.QLabel(self.frame_22)
        self.lblIDValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblIDValidation.setText("")
        self.lblIDValidation.setObjectName("lblIDValidation")
        self.verticalLayout_19.addWidget(self.lblIDValidation)
        self.verticalLayout_7.addWidget(self.frame_22)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_80 = QtWidgets.QLabel(self.frame_11)
        self.label_80.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("color:#48ACAC")
        self.label_80.setObjectName("label_80")
        self.verticalLayout_8.addWidget(self.label_80)
        self.frame_25 = QtWidgets.QFrame(self.frame_11)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_22.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_22.setSpacing(1)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.txtEmail = QtWidgets.QLineEdit(self.frame_25)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtEmail.setFont(font)
        self.txtEmail.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtEmail.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.txtEmail.setPlaceholderText("")
        self.txtEmail.setObjectName("txtEmail")
        self.verticalLayout_22.addWidget(self.txtEmail)
        self.lblEmailValidation = QtWidgets.QLabel(self.frame_25)
        self.lblEmailValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblEmailValidation.setText("")
        self.lblEmailValidation.setObjectName("lblEmailValidation")
        self.verticalLayout_22.addWidget(self.lblEmailValidation)
        self.verticalLayout_8.addWidget(self.frame_25)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_81 = QtWidgets.QLabel(self.frame_12)
        self.label_81.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color:#48ACAC")
        self.label_81.setObjectName("label_81")
        self.verticalLayout_9.addWidget(self.label_81)
        self.frame_28 = QtWidgets.QFrame(self.frame_12)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_25.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_25.setSpacing(1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.txtCellNo = QtWidgets.QLineEdit(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtCellNo.setFont(font)
        self.txtCellNo.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtCellNo.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txtCellNo.setMaxLength(12)
        self.txtCellNo.setObjectName("txtCellNo")
        self.verticalLayout_25.addWidget(self.txtCellNo)
        self.txtCellNoValidation = QtWidgets.QLabel(self.frame_28)
        self.txtCellNoValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.txtCellNoValidation.setText("")
        self.txtCellNoValidation.setObjectName("txtCellNoValidation")
        self.verticalLayout_25.addWidget(self.txtCellNoValidation)
        self.verticalLayout_9.addWidget(self.frame_28)
        self.verticalLayout_4.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_5)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_82 = QtWidgets.QLabel(self.frame_13)
        self.label_82.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setStyleSheet("color:#48ACAC")
        self.label_82.setText("")
        self.label_82.setObjectName("label_82")
        self.verticalLayout_10.addWidget(self.label_82)
        self.frame_31 = QtWidgets.QFrame(self.frame_13)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_28.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_28.setSpacing(1)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.lblDateValidation = QtWidgets.QLabel(self.frame_31)
        self.lblDateValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblDateValidation.setText("")
        self.lblDateValidation.setObjectName("lblDateValidation")
        self.verticalLayout_28.addWidget(self.lblDateValidation)
        self.verticalLayout_10.addWidget(self.frame_31)
        self.verticalLayout_4.addWidget(self.frame_13)
        self.horizontalLayout.addWidget(self.frame_5)
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
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
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
        self.frame_23 = QtWidgets.QFrame(self.frame_14)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_20.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_20.setSpacing(1)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.txtName = QtWidgets.QLineEdit(self.frame_23)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtName.setFont(font)
        self.txtName.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtName.setPlaceholderText("")
        self.txtName.setObjectName("txtName")
        self.verticalLayout_20.addWidget(self.txtName)
        self.lblNameValidation = QtWidgets.QLabel(self.frame_23)
        self.lblNameValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblNameValidation.setText("")
        self.lblNameValidation.setObjectName("lblNameValidation")
        self.verticalLayout_20.addWidget(self.lblNameValidation)
        self.verticalLayout_11.addWidget(self.frame_23)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_6)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
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
        self.frame_26 = QtWidgets.QFrame(self.frame_15)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_23.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_23.setSpacing(1)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.txtUserName = QtWidgets.QLineEdit(self.frame_26)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtUserName.setFont(font)
        self.txtUserName.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtUserName.setPlaceholderText("")
        self.txtUserName.setObjectName("txtUserName")
        self.verticalLayout_23.addWidget(self.txtUserName)
        self.lblUserNameValidation = QtWidgets.QLabel(self.frame_26)
        self.lblUserNameValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblUserNameValidation.setText("")
        self.lblUserNameValidation.setObjectName("lblUserNameValidation")
        self.verticalLayout_23.addWidget(self.lblUserNameValidation)
        self.verticalLayout_12.addWidget(self.frame_26)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_6)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
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
        self.frame_29 = QtWidgets.QFrame(self.frame_16)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_26.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_26.setSpacing(1)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.txtSalary = QtWidgets.QLineEdit(self.frame_29)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtSalary.setFont(font)
        self.txtSalary.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtSalary.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txtSalary.setPlaceholderText("")
        self.txtSalary.setObjectName("txtSalary")
        self.verticalLayout_26.addWidget(self.txtSalary)
        self.lblSalaryValidation = QtWidgets.QLabel(self.frame_29)
        self.lblSalaryValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblSalaryValidation.setText("")
        self.lblSalaryValidation.setObjectName("lblSalaryValidation")
        self.verticalLayout_26.addWidget(self.lblSalaryValidation)
        self.verticalLayout_13.addWidget(self.frame_29)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_6)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_86 = QtWidgets.QLabel(self.frame_17)
        self.label_86.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setStyleSheet("color:#48ACAC")
        self.label_86.setText("")
        self.label_86.setObjectName("label_86")
        self.verticalLayout_14.addWidget(self.label_86)
        self.frame_32 = QtWidgets.QFrame(self.frame_17)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_29.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_29.setSpacing(1)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.lblAreaValidation = QtWidgets.QLabel(self.frame_32)
        self.lblAreaValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblAreaValidation.setText("")
        self.lblAreaValidation.setObjectName("lblAreaValidation")
        self.verticalLayout_29.addWidget(self.lblAreaValidation)
        self.verticalLayout_14.addWidget(self.frame_32)
        self.verticalLayout_5.addWidget(self.frame_17)
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
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
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
        self.frame_24 = QtWidgets.QFrame(self.frame_18)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_21.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_21.setSpacing(1)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.txtCNIC = QtWidgets.QLineEdit(self.frame_24)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtCNIC.setFont(font)
        self.txtCNIC.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtCNIC.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtCNIC.setMaxLength(98889)
        self.txtCNIC.setObjectName("txtCNIC")
        self.verticalLayout_21.addWidget(self.txtCNIC)
        self.lblCNICValidation = QtWidgets.QLabel(self.frame_24)
        self.lblCNICValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblCNICValidation.setText("")
        self.lblCNICValidation.setObjectName("lblCNICValidation")
        self.verticalLayout_21.addWidget(self.lblCNICValidation)
        self.verticalLayout_15.addWidget(self.frame_24)
        self.verticalLayout_6.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_7)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_88 = QtWidgets.QLabel(self.frame_19)
        self.label_88.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("color:#48ACAC")
        self.label_88.setObjectName("label_88")
        self.verticalLayout_16.addWidget(self.label_88)
        self.frame_27 = QtWidgets.QFrame(self.frame_19)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_24.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_24.setSpacing(1)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.txtPassword = QtWidgets.QLineEdit(self.frame_27)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPassword.setFont(font)
        self.txtPassword.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtPassword.setMaxLength(12)
        self.txtPassword.setObjectName("txtPassword")
        self.verticalLayout_24.addWidget(self.txtPassword)
        self.lblPasswordValidation = QtWidgets.QLabel(self.frame_27)
        self.lblPasswordValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblPasswordValidation.setText("")
        self.lblPasswordValidation.setObjectName("lblPasswordValidation")
        self.verticalLayout_24.addWidget(self.lblPasswordValidation)
        self.verticalLayout_16.addWidget(self.frame_27)
        self.verticalLayout_6.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_7)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.cmbx = QtWidgets.QLabel(self.frame_20)
        self.cmbx.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cmbx.setFont(font)
        self.cmbx.setStyleSheet("color:#48ACAC")
        self.cmbx.setObjectName("cmbx")
        self.verticalLayout_17.addWidget(self.cmbx)
        self.frame_30 = QtWidgets.QFrame(self.frame_20)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_27.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_27.setSpacing(1)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.dateEditAddAgent = QtWidgets.QDateEdit(self.frame_30)
        self.dateEditAddAgent.setMinimumSize(QtCore.QSize(0, 30))
        self.dateEditAddAgent.setMaximumSize(QtCore.QSize(16777215, 40))
        self.dateEditAddAgent.setObjectName("dateEditAddAgent")
        self.verticalLayout_27.addWidget(self.dateEditAddAgent)
        self.lblVehicleValidation = QtWidgets.QLabel(self.frame_30)
        self.lblVehicleValidation.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblVehicleValidation.setText("")
        self.lblVehicleValidation.setObjectName("lblVehicleValidation")
        self.verticalLayout_27.addWidget(self.lblVehicleValidation)
        self.verticalLayout_17.addWidget(self.frame_30)
        self.verticalLayout_6.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_7)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.cmbx_2 = QtWidgets.QLabel(self.frame_21)
        self.cmbx_2.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cmbx_2.setFont(font)
        self.cmbx_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.cmbx_2.setObjectName("cmbx_2")
        self.verticalLayout_18.addWidget(self.cmbx_2)
        self.frame_33 = QtWidgets.QFrame(self.frame_21)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_30.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_30.setSpacing(1)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.txtID_2 = QtWidgets.QLineEdit(self.frame_33)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtID_2.setFont(font)
        self.txtID_2.setStyleSheet("background-color:white;\n"
"border:none;\n"
"\n"
"color:black;\n"
"padding-bottom:7px;")
        self.txtID_2.setReadOnly(True)
        self.txtID_2.setPlaceholderText("")
        self.txtID_2.setObjectName("txtID_2")
        self.verticalLayout_30.addWidget(self.txtID_2)
        self.label_12 = QtWidgets.QLabel(self.frame_33)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_30.addWidget(self.label_12)
        self.verticalLayout_18.addWidget(self.frame_33)
        self.verticalLayout_6.addWidget(self.frame_21)
        self.horizontalLayout.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(-1, 50, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2.addWidget(self.frame_9)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnCancel = QtWidgets.QPushButton(self.frame_8)
        self.btnCancel.setMinimumSize(QtCore.QSize(0, 35))
        self.btnCancel.setMaximumSize(QtCore.QSize(300, 200))
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
"border-radius:20px;\n"
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
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnAdd = QtWidgets.QPushButton(self.frame_8)
        self.btnAdd.setMinimumSize(QtCore.QSize(0, 35))
        self.btnAdd.setMaximumSize(QtCore.QSize(300, 250))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.btnAdd.setFont(font)
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("#btnAdd\n"
"{\n"
"\n"
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
        self.horizontalLayout_2.addWidget(self.frame_8, 0, QtCore.Qt.AlignTop)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_65.setText(_translate("MainWindow", "Add New Manager"))
        self.label_79.setText(_translate("MainWindow", "ID"))
        self.txtID.setPlaceholderText(_translate("MainWindow", "M"))
        self.label_80.setText(_translate("MainWindow", "Email"))
        self.label_81.setText(_translate("MainWindow", "Cell No"))
        self.txtCellNo.setPlaceholderText(_translate("MainWindow", "+92323*******"))
        self.label_83.setText(_translate("MainWindow", "Name"))
        self.label_84.setText(_translate("MainWindow", "User Name"))
        self.label_85.setText(_translate("MainWindow", "Salary"))
        self.label_87.setText(_translate("MainWindow", "CNIC"))
        self.txtCNIC.setPlaceholderText(_translate("MainWindow", "13 Digits without dashes"))
        self.label_88.setText(_translate("MainWindow", "Password"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "Minimum of 8 Character"))
        self.cmbx.setText(_translate("MainWindow", "Date"))
        self.cmbx_2.setText(_translate("MainWindow", "Vehicle"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
import resources_rc
