
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from UserInterface import GuiWindow
import time

###
#   Main File for GUI 
#
###

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GuiWindow()
    app.exec_()
