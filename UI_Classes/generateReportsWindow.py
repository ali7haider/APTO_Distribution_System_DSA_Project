# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:44:37 2024

@author: Digital Zone
"""

import os
from PyQt5.QtWidgets import QMainWindow,QFileDialog
from UI_Classes.generateReportsWindow_ui import Ui_MainWindow
from DL.SalesManDL import salesManDL
from BL.file_paths import FilePaths
from datetime import date
from DL.OrderDispatcherDL import orderDispatcherDL
from DL.DeliveryManDL import deliveryManDL
from DL.ManagerDL import managerDL
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5.QtGui import QPixmap
from fpdf import FPDF
from datetime import timedelta
import pandas as pd

class GenerateReportWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(GenerateReportWindow,self).__init__()
        self.setupUi(self)
        self.file_paths = FilePaths(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data')))  
      
        self.btnSalesinLast7DaysTabular.clicked.connect(lambda:self.printLast7DaySaleTabularForm())
        self.btnSalesinLast7DaysGraph.clicked.connect(lambda:self.printLast7DaySaleReports())
        self.btnAllEmployeeGraph.clicked.connect(lambda:self.printAllEmployeesGraph())

    def printAllEmployeesGraph(self):
        employees=["Manager","Sales Agent","Order Dispatcher","Delivery Man"]
        num=[]
        num.append(managerDL().managerCount)
        num.append(salesManDL().saleAgentCount)
        num.append(orderDispatcherDL().oderDispactherCount)
        num.append(deliveryManDL().deliveryManCount)
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            add=fileNames[0]+"/AllEmployeesGraph.pdf"
            with PdfPages(add) as export_pdf:
                colors = ['#8CDBA9','#4E9C81','#49DCB1','#00917C']
                plt.figure(figsize=(8,6))
                explode = (0, 0.1, 0, 0)       
                fig1, ax1 = plt.subplots()
                ax1.pie(num, explode=explode, labels=employees,colors=colors ,autopct='%1.1f%%',
                shadow=True, startangle=90)
                ax1.axis('equal')        
                # plt.grid(True)
                export_pdf.savefig()
                plt.close()
                self.close()
    
    def printLast7DaySaleReports(self):
        df=pd.read_csv(self.file_paths.SalesPerDate,header=None,usecols=[0,1],infer_datetime_format=True)
        sales=df[0].values.tolist()
        dates=df[1].values.tolist()
        sa=[]
        da=[]
        dateToday= date.today()
        today = date.today()
        for i in range(7):
            yesterday =(today - timedelta(days = i+1)).strftime("%d/%m/%Y")
            tSum=0
            for j in range(len(dates)):
                if dates[j]==str(yesterday):
                    tSum=tSum+int(sales[j])
            
            sa.append(tSum) 
            da.append(yesterday)
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            add=fileNames[0]+"/SalesInLast7DaysGraph.pdf"
            with PdfPages(add) as export_pdf:
                plt.figure(figsize=(10,6))
                plt.xlabel("Date",fontsize=14)
                plt.ylabel("Sales",fontsize=14)
                plt.bar(da,sa,color='#48ACAC')
                # plt.grid(True)
                export_pdf.savefig()
                plt.close()
                self.close()
    
    def printLast7DaySaleTabularForm(self):
        pdf=FPDF(format='letter', unit='in',orientation='L')
        pdf.add_page()
        # pdf.image('logoApto.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
        epw = pdf.w - 2*pdf.l_margin
        col_width = epw/7.9
        today=date.today()
         
        header=['Days','Date','Juices & Food Drinks','Nestle Water','Coffee','Breakfast Cereals','Infant Nutrition','Total']
        data = [
        ['Monday','2022-12-24',"123",'12','15','0','0','0'],
        ['Tuesday','2022-12-24',"123",'12','15','12','200','0'],
        ['Wednesday','2022-12-24',"123",'12','15','12','200','0'],
        ['Thursday','2022-12-24',"123",'12','15','12','200','0'],
        ['Friday','2022-12-24',"123",'12','15','12','200','0'],
        ['Saturday','2022-12-24',"123",'12','15','12','200','0'],
        ['Sunday','2022-12-24',"123",'12','15','12','200','0'],
        ['Total','N/A',"123",'12','15','12','200','0']
        ]
        df=pd.read_csv(self.file_paths.SalesPerDate,header=None,usecols=[0,1,2],infer_datetime_format=True)
        sales=df[0].values.tolist()
        dates=df[1].values.tolist()
        category=df[2].values.tolist()
        tJuices=0
        tCofee=0
        tInfant=0
        tWater=0
        tCereals=0
        
        for i in range(7):
            yesterday =(today - timedelta(days = i+1)).strftime("%d/%m/%Y")
            df = pd.Timestamp(yesterday)
            day=df.day_name()
            data[i][0]=day
            data[i][1]=yesterday
            for j in range(len(dates)):
                if dates[j]==str(yesterday):
                    print("Date True")
                    if category[j]=="Juices & Food Drinks":
                        tJuices=tJuices+sales[j]
                    if category[j]=="Coffee":
                        tCofee=tCofee+sales[j]
                    if category[j]=="Infant Nutrition":
                        tInfant=tInfant+sales[j]
                    if category[j]=="Cereals":
                        tCereals=tCereals+sales[j]
                    if category[j]=="Nestle Water":
                        tWater=tWater+sales[j]
            data[i][2]=tJuices
            data[i][3]=tWater
            data[i][4]=tCofee
            data[i][5]=tCereals
            data[i][6]=tInfant
            total=int(tJuices)+int(tWater)+int(tCofee)+int(tCereals)+int(tInfant)
            data[i][7]=total
            tJuices=0
            tCofee=0
            tWater=0
            tInfant=0
            tCereals=0
        col=2
        tSum=0
        for i in range(5):
            tSum=0
            for j in range(7):
                tSum=data[j][col]+tSum
            data[7][col]=tSum
            col=col+1
                        
        
        #
        th = pdf.font_size
        # Line break equivalent to 4 lines
        pdf.ln(4*th)
        pdf.set_font('Times','B',30.0) 
        pdf.cell(epw, 0.0, 'APTO Distribution', align='C')
        pdf.ln(1.0)
        pdf.set_font('Times','B',20.0) 
        pdf.cell(epw, 0.0, 'Weekly Sales Statistics', align='C')
        pdf.set_font('Times','B',10.0) 
        pdf.ln(0.5)
        for datum in header:
                # Enter data in colums
                pdf.cell(col_width, 2*th, str(datum), border=1)
        pdf.set_font('Times','',10.0) 
        pdf.ln(2*th)
        for row in data:
            for datum in row:
                    # Enter data in colums
                    if datum=="Total":
                        pdf.set_font('Times','B',10.0)                     
                    pdf.cell(col_width, 2*th, str(datum), border=1)
            pdf.ln(2*th)   
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            add=fileNames[0]+"/SalesInLast7Tabular.pdf"
            pdf.output(add,'F')
            self.close()
    def loadReports(self):
        df=pd.read_csv(self.file_paths.SalesPerDate,header=None,usecols=[0,1],infer_datetime_format=True)
        sales=df[0].values.tolist()
        dates=df[1].values.tolist()
        sa=[]
        da=[]
        dateToday= date.today()
        today = date.today()
        for i in range(7):
            yesterday =(today - timedelta(days = i+1)).strftime("%d/%m/%Y")
            tSum=0
            for j in range(len(dates)):
                if dates[j]==str(yesterday):
                    tSum=tSum+int(sales[j])
            
            sa.append(tSum) 
            da.append(yesterday)
        plt.figure(figsize=(10,5))
        plt.xlabel("Date",fontsize=14)
        plt.ylabel("Sales",fontsize=14)
        plt.bar(da,sa,color='#48ACAC')
        plt.savefig("salesLast7Days.png", transparent=True)
        # pixmap=QPixmap("save_figure.png")
        # item = QGraphicsPixmapItem(pixmap)
        # scene.addItem(item)
        pixmap = QPixmap('salesLast7Days.png')        
        self.lblSalePerDay.setPixmap(pixmap)