import sys

from Ui_test2 import *
from kit_class import *
from youtube import *



downloaddata = []
API_KEY = "AIzaSyDFC_QxH093_VthlLPWvC2BmzPP0hhbX9U"




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
btn = Btn(MainWindow)
MainWindow.show()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)

yt = youtube(API_KEY)

list1 = Kit(ui)
list1.add_download_list(downloaddata)

app.exec_()