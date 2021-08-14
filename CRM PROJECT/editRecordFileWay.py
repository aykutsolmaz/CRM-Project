import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox

from UieditRecordFileWay import Ui_editRecodFileWayUi



class ERFW_Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_editRecodFileWayUi()
        self.ui.setupUi(self)

        with open('pathFolder.txt', 'r', encoding="utf-8") as file:
            pathRFW = file.readlines()
            self.ui.line_recordPath.setText(pathRFW[1])

        self.ui.fileBrowse_BtnRFW.clicked.connect(self.openFolderChoice)
        self.ui.filePathSave_BtnRFW.clicked.connect(self.saveFolderPath)
    
    def openFolderChoice(self):
        filePath = QFileDialog.getExistingDirectory(self, "Kayıt Konumu Seç")
        self.ui.line_recordPath.setText(filePath)
    
    def saveFolderPath(self):
        with open('pathFolder.txt', 'r+', encoding="utf-8") as file:
            data = file.readlines()
            dataSecondLine = data[1]

        with open('pathFolder.txt', 'r+', encoding="utf-8") as file:
            newPath = self.ui.line_recordPath.text() + "\n"
            tempdata = file.read()
            #print(tempdata)
            file.seek(0)
            dataChange = tempdata.replace(dataSecondLine, newPath)           
            file.write(dataChange)
            file.truncate()

        self.ui.statusbar.showMessage("Kayıt yapılacak konum kaydedildi.",2000)
    