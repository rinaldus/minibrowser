#!/usr/bin/env python3

from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout, QSizeGrip, QFileDialog)
from PyQt5.QtCore import (QThread, QTimer, QFile, QSettings,Qt, QPoint )
import resources_rc
from ui_widget import Ui_MiniBrowserWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import random
import fnmatch

programSettings = QSettings(os.path.expanduser("~")+"/.config/minibrowser/settings.conf", QSettings.NativeFormat)
MainWindowType = QtCore.Qt.Tool

def SettingsExist():
    if (programSettings.contains("SizeX") and
        programSettings.contains("SizeY") and
        programSettings.contains("PosX") and
        programSettings.contains("PosY")):
        return True
    else:
        return False

def SettingsSave():
    programSettings.setValue("SizeX",window.geometry().width())
    programSettings.setValue("SizeY",window.geometry().height())
    programSettings.setValue("PosX",window.x())
    programSettings.setValue("PosY",window.y())

#Settings load

if (SettingsExist()):
    SizeX = int(programSettings.value("SizeX"))
    SizeY = int(programSettings.value("SizeY"))
    PosX = int(programSettings.value("PosX"))
    PosY = int(programSettings.value("PosY"))
else:
    SizeX = 800
    SizeY = 600
    PosX = 50
    PosY = 50

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        
        # Init
        
        self.ui = Ui_MiniBrowserWidget()
        self.ui.setupUi(self)
        self.setWindowFlags(MainWindowType | Qt.FramelessWindowHint)
        self.locked = True
        self.resize(SizeX, SizeY)
        self.move(PosX,PosY)
        # Widget configuration
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
        
        
    # Functions    
    def showMenu(self,point):
            menu = QMenu(self)
            if self.locked:
                menu.addAction(QAction(QIcon(':icons/unlock.png'),"&Unlock", self, triggered=self.Unlock))
            else:
                menu.addAction(QAction(QIcon(':icons/lock.png'),"&Lock", self, triggered=self.Lock))
            menu.addAction(QAction(QIcon(':icons/settings.png'),"&Settings", self, triggered=self.dummy))
            menu.addAction(QAction(QIcon(':icons/quit.png'),"&Quit", self, triggered=QApplication.instance().quit))
            menu.popup(self.mapToGlobal(point))
        
    def Unlock(self):
        window.setWindowFlags(QtCore.Qt.Window)
        self.locked = False
        window.show()
        
    def Lock(self):
        window.setWindowFlags(MainWindowType | Qt.FramelessWindowHint)
        self.locked = True
        window.show()
        
    def dummy(self):
        print("settings.show")
        
    def closeEvent(self, event):
        SettingsSave()
        QApplication.instance().quit()
            
    def resizeEvent(self,event):
        programSettings.setValue("SizeX",window.geometry().width())
        programSettings.setValue("SizeY",window.geometry().height())
        
    def moveEvent(self,event):
        if (self.locked):
        # The following hack is for KWin 5.x because it can move even locked windows, even frameless windows. Now if you try to move locked window, it goes back.
            if (SettingsExist()):
                self.move(int(programSettings.value("PosX")),int(programSettings.value("PosY")))
            else:
                self.move(PosX,PosY)
            event.ignore()
        programSettings.setValue("PosX",window.x())
        programSettings.setValue("PosY",window.y())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(True)
    window = Window()
    window.show()
    sys.exit(app.exec_())
