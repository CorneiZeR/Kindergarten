# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mian.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.admin_button = QtWidgets.QPushButton(self.centralwidget)
        self.admin_button.setObjectName("admin_button")
        self.verticalLayout.addWidget(self.admin_button)
        self.employee_button = QtWidgets.QPushButton(self.centralwidget)
        self.employee_button.setObjectName("employee_button")
        self.verticalLayout.addWidget(self.employee_button)
        self.child_button = QtWidgets.QPushButton(self.centralwidget)
        self.child_button.setObjectName("child_button")
        self.verticalLayout.addWidget(self.child_button)
        self.employes_button = QtWidgets.QPushButton(self.centralwidget)
        self.employes_button.setObjectName("employes_button")
        self.verticalLayout.addWidget(self.employes_button)
        self.children_button = QtWidgets.QPushButton(self.centralwidget)
        self.children_button.setObjectName("children_button")
        self.verticalLayout.addWidget(self.children_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????????????"))
        self.admin_button.setText(_translate("MainWindow", "??????????????"))
        self.employee_button.setText(_translate("MainWindow", "?????????? ????????????????????"))
        self.child_button.setText(_translate("MainWindow", "?????????? ??????????????"))
        self.employes_button.setText(_translate("MainWindow", "????????????????????"))
        self.children_button.setText(_translate("MainWindow", "????????"))
