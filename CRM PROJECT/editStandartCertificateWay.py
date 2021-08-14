import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox

from UiEditStandartCertificateWay import Ui_editStandartCertificateWayUi

class ESCW_Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_editStandartCertificateWayUi()
        self.ui.setupUi(self)

        with open('pathFolder.txt', 'r', encoding="utf-8") as file:
            pathSCW = file.readlines()
            self.ui.line_filePath.setText(pathSCW[0])
            
        self.ui.fileBrowse_Btn.clicked.connect(self.openFolderChoice)
        self.ui.filePathSave_Btn.clicked.connect(self.saveFolderPath)

    def openFolderChoice(self):
        filePath = QFileDialog.getExistingDirectory(self, "Standart Sertifika Konumu Seç")
        self.ui.line_filePath.setText(filePath)
    
    def saveFolderPath(self):
        with open('pathFolder.txt', 'r+', encoding="utf-8") as file:
            data = file.readlines()
            dataFirstLine = data[0]
        
        with open('pathFolder.txt', 'r+', encoding="utf-8") as file:
            newPath = self.ui.line_filePath.text() + "\n"
            tempdata = file.read()
            #print(tempdata)
            file.seek(0)
            dataChange = tempdata.replace(dataFirstLine, newPath)           
            file.write(dataChange)
            file.truncate()

        self.ui.statusbar.showMessage("Standart sertifikalar konumu kaydedildi.",2000)
