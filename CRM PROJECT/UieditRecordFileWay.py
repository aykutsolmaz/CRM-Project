# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UieditRecordFileWay.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editRecodFileWayUi(object):
    def setupUi(self, editRecodFileWayUi):
        editRecodFileWayUi.setObjectName("editRecodFileWayUi")
        editRecodFileWayUi.resize(590, 135)
        editRecodFileWayUi.setMinimumSize(QtCore.QSize(590, 135))
        editRecodFileWayUi.setMaximumSize(QtCore.QSize(590, 135))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/rpath.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        editRecodFileWayUi.setWindowIcon(icon)
        editRecodFileWayUi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(editRecodFileWayUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(35, 15, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_recordPath = QtWidgets.QLineEdit(self.centralwidget)
        self.line_recordPath.setGeometry(QtCore.QRect(30, 50, 551, 21))
        self.line_recordPath.setText("")
        self.line_recordPath.setReadOnly(True)
        self.line_recordPath.setObjectName("line_recordPath")
        self.fileBrowse_BtnRFW = QtWidgets.QPushButton(self.centralwidget)
        self.fileBrowse_BtnRFW.setGeometry(QtCore.QRect(410, 80, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.fileBrowse_BtnRFW.setFont(font)
        self.fileBrowse_BtnRFW.setStyleSheet("QPushButton{\n"
"border-radius: 3px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-top: 1px solid rgb(0, 0, 0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"border-left: 1px solid rgb(0, 0, 0);\n"
"border-right: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(230, 230, 230, 252);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(200, 200, 200);\n"
"}")
        self.fileBrowse_BtnRFW.setObjectName("fileBrowse_BtnRFW")
        self.filePathSave_BtnRFW = QtWidgets.QPushButton(self.centralwidget)
        self.filePathSave_BtnRFW.setGeometry(QtCore.QRect(500, 80, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.filePathSave_BtnRFW.setFont(font)
        self.filePathSave_BtnRFW.setStyleSheet("QPushButton{\n"
"border-radius: 3px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-top: 1px solid rgb(0, 0, 0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"border-left: 1px solid rgb(0, 0, 0);\n"
"border-right: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(230, 230, 230, 252);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(200, 200, 200);\n"
"}")
        self.filePathSave_BtnRFW.setObjectName("filePathSave_BtnRFW")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 40, 550, 5))
        self.line_2.setMinimumSize(QtCore.QSize(0, 5))
        self.line_2.setMaximumSize(QtCore.QSize(550, 5))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        editRecodFileWayUi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(editRecodFileWayUi)
        self.statusbar.setObjectName("statusbar")
        editRecodFileWayUi.setStatusBar(self.statusbar)

        self.retranslateUi(editRecodFileWayUi)
        QtCore.QMetaObject.connectSlotsByName(editRecodFileWayUi)

    def retranslateUi(self, editRecodFileWayUi):
        _translate = QtCore.QCoreApplication.translate
        editRecodFileWayUi.setWindowTitle(_translate("editRecodFileWayUi", "Kayıt Dosyalarının Konumu"))
        self.label.setText(_translate("editRecodFileWayUi", "Kayıtların Bulunduğu Konum"))
        self.fileBrowse_BtnRFW.setText(_translate("editRecodFileWayUi", "DOSYA SEÇ"))
        self.filePathSave_BtnRFW.setText(_translate("editRecodFileWayUi", "KAYIT"))
import icons_rc
