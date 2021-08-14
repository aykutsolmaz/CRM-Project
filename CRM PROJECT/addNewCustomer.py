import sys
import os
import pandas as pd

from openpyxl import Workbook, load_workbook
#from openpyxl.worksheet.worksheet import Worksheet
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from UiAddNewCustomer import Ui_addNewCustomerUi

dfhosisno = pd.read_excel('calibration_info.xlsx','hospitals')

class ANC_ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_addNewCustomerUi()
        self.ui.setupUi(self)

        validator = QRegExpValidator(QRegExp(r'^[A-Z]*$'))      
        self.ui.customerCode.setValidator(validator)

        r = int(dfhosisno["isno"].max())

        self.ui.customerOrder.setText(str(r + 1))
        self.ui.add_record.clicked.connect(self.addNewCustomer)

    def addNewCustomer(self):

        search_value4 = dfhosisno["kod"].isin([self.ui.customerCode.text()]).any()

        addposition = str(len(pd.read_excel('calibration_info.xlsx','hospitals')) + 2)
        isno = self.ui.customerOrder.text()
        customercode = self.ui.customerCode.text()
        customeraddress = self.ui.customerAddres.text()
        customername = self.ui.customerName.text()
        
        if customercode == "" or customeraddress == "" or customername == "":
            self.statusBar().showMessage("Bilgileri Eksiksiz Giriniz...", 3000)
        elif search_value4 == True:
            self.statusBar().showMessage("Müşteri Kodu Benzersiz Olmalı. Başka Bir Kod Deneyiniz", 3000)
        else:
            calibrationInfoExcel = load_workbook("calibration_info.xlsx")
            worksheet = calibrationInfoExcel.active
            worksheet = calibrationInfoExcel["hospitals"]
            
            worksheet["A" + addposition] = int(isno)
            worksheet["B" + addposition] = customeraddress
            worksheet["C" + addposition] = customername
            worksheet["D" + addposition] = customercode

            calibrationInfoExcel.save("calibration_info.xlsx")
            calibrationInfoExcel.close()
            self.statusBar().showMessage("Müşteri Kaydedildi.", 3000)
        

        
