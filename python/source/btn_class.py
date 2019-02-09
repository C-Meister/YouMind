from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request


class Btn(QtWidgets.QMainWindow):

    def __init__(self,ui):
        super().__init__()
        self.ui = ui 

    