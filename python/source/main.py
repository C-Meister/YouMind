import sys

from Ui_test2 import *
from kit_class import *
from btn_class import *
from youtube import *



downloaddata = []
API_KEY = "AIzaSyCb0j6QKRcOvfqpeta1slWJZCrj6xIkD5Y"



if __name__ == "__main__":

	list1 = 0
    
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	yt = youtube(API_KEY)
	btn = Btn(MainWindow)
	MainWindow.show()

	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)

	

	

	list1 = Kit(ui)
	#list1.add_download_list(yt.get_videos('https://www.youtube.com/channel/UCMRdlwfhLECvQw0FN0s_csg'))
	btn.btn_add(list1, yt)


	app.exec_()