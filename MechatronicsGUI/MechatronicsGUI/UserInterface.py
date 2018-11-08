import sys
from PyQt5.QtWidgets import QProgressBar, QTextEdit, QCheckBox, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QComboBox, QLabel, QStyleFactory
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QThread

class GuiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Mouse Detection'
        self.left = 10
        self.top = 10
        self.width = 1200
        self.height = 600

        self.folderName = ""
        self.viewVideo = False
        self.clickedButton = False
        self.initUI()
        self.workerThread = WorkerThread(None, self)
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Folder TextBox
        self.textbox = QLineEdit(r"Command Here", self)
        self.textbox.move(20, 440)
        self.textbox.resize(900,20)

        # Create a button in the window
        self.button = QPushButton('Send', self)
        self.button.move(1080,440)

        # Combo box (drop down box)
        comboBox = QComboBox(self)
        comboBox.addItem("Boat")
        comboBox.addItem("Drone")
        comboBox.move(930, 440)

        # Log Of How The program is doing
        self.log = QTextEdit(self)
        self.log.setReadOnly(True)
        self.log.move(20, 480)
        self.log.resize(1160, 100)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
        self.initMessage()
 
    @pyqtSlot()
    def on_click(self):
        self.logMessage("Sent: {}".format(self.textbox.text()))

        self.workerThread.start()

    def logMessage(self, msg):
        self.log.append(msg)

    def getClickedButton(self):
        return self.clickedButton

    def initMessage(self):
        self.logMessage("Hub for autonomous drone and boat")
        self.logMessage("Cardiff University 4th Year Project 2018/2019")
 
class WorkerThread(QThread):

    def __init__(self, parent=None, guiWindow=None):
        super(WorkerThread, self).__init__(parent)
        self.guiWindow = guiWindow

    def run(self):
        self.guiWindow.logMessage("NewThread")
        #def getTrackingTimes(fileName, showVideo, gui):
        #track, videos = MouseDetectObject.getTrackingTimes(self.guiWindow.folderName, self.guiWindow.viewVideo, self.guiWindow)