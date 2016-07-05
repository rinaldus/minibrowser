# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/widget.ui'
#
# Created by: PyQt5 UI code generator 5.6.1.dev1604271126
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MiniBrowserWidget(object):
    def setupUi(self, MiniBrowserWidget):
        MiniBrowserWidget.setObjectName("MiniBrowserWidget")
        MiniBrowserWidget.resize(665, 483)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MiniBrowserWidget.sizePolicy().hasHeightForWidth())
        MiniBrowserWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MiniBrowserWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.browser = QtWebKitWidgets.QWebView(MiniBrowserWidget)
        self.browser.setUrl(QtCore.QUrl("http://yandex.ru/"))
        self.browser.setObjectName("browser")
        self.verticalLayout.addWidget(self.browser)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(MiniBrowserWidget)
        QtCore.QMetaObject.connectSlotsByName(MiniBrowserWidget)

    def retranslateUi(self, MiniBrowserWidget):
        _translate = QtCore.QCoreApplication.translate
        MiniBrowserWidget.setWindowTitle(_translate("MiniBrowserWidget", "Mini Browser"))

from PyQt5 import QtWebKitWidgets
import resources_rc
