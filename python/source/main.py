import sys

from Ui_test2 import *
from kit_class import *
from btn_class import *
from youtube import *


downloaddata = []
API_KEY = "AIzaSyAasuN7ChDi_8Hemxv1Dd9-troI6-Fe-7M"



if __name__ == "__main__":

	
	list1 = 0

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	yt = youtube(API_KEY,"C:\\Users\\ShinSH\\Desktop\\test\\")
	btn = Btn(MainWindow)
	MainWindow.show()

	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)

	

	

	list1 = Kit(ui)
	#list1.add_download_list(yt.get_videos('https://www.youtube.com/channel/UCMRdlwfhLECvQw0FN0s_csg'))
	btn.btn_add(list1, yt)


	app.exec_()