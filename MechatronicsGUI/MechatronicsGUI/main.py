
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory
import sys
from UserInterface import GuiWindow
import time

###
#   Main File for GUI 
#
###

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = GuiWindow()
    app.exec_()
