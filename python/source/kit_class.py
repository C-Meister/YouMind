
from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request



class Kit(QtWidgets.QMainWindow):
    

    def __init__(self,ui):
        super().__init__()
        self.ui = ui   





    def add_download_list(self,downloaddata): #함수명 알아서 바꾸셈
        
        length = len(downloaddata)
        
        self.ui.linked_p = [QtWidgets.QWidget(self.ui.layout_link_data) for i in range(length)]


        for i in range(length):
            self.ui.linked_p[i] = QtWidgets.QWidget(self.ui.layout_link_data)
            self.ui.linked_p[i].setMinimumSize(QtCore.QSize(0, 120))
            self.ui.linked_p[i].setMaximumSize(QtCore.QSize(16777215, 120))
            self.ui.linked_p[i].setObjectName("linked_p")


        self.ui.linked_image = [QtWidgets.QLabel(self.ui.linked_p[i]) for i in range(length)]
        self.ui.linked_title = [QtWidgets.QLabel(self.ui.linked_p[i]) for i in range(length)]
        self.ui.linked_youtube_icon = [QtWidgets.QLabel(self.ui.linked_p[i]) for i in range(length)]
        self.ui.linked_id = [QtWidgets.QLabel(self.ui.linked_p[i]) for i in range(length)]


        for i in range(length):  
            self.ui.linked_image[i].setGeometry(QtCore.QRect(10, 10, 160, 90))
            self.ui.linked_image[i].setStyleSheet("background-color : black ;")
            self.ui.linked_image[i].setObjectName("linked_image")

            url = downloaddata[i]['thumbnail']
            tmp_data = urllib.request.urlopen(url).read()

            tmp_image = QtGui.QImage()
            tmp_image.loadFromData(tmp_data)

            self.ui.linked_image[i].setPixmap(QtGui.QPixmap(tmp_image))
            self.ui.linked_image[i].setScaledContents(True)

            self.ui.linked_title[i].setGeometry(QtCore.QRect(180, 10, 361, 71))
            self.ui.linked_title[i].setText(downloaddata[i]['title'])
            font = QtGui.QFont()
            font.setFamily("서울남산체 EB")
            font.setPointSize(16)
            self.ui.linked_title[i].setFont(font)
            self.ui.linked_title[i].setScaledContents(False)
            self.ui.linked_title[i].setWordWrap(True)
            self.ui.linked_title[i].setObjectName("linked_title")
            
            self.ui.linked_youtube_icon[i].setGeometry(QtCore.QRect(182, 80, 21, 21))
            self.ui.linked_youtube_icon[i].setStyleSheet("image:url(./image/sub1.png);")
            self.ui.linked_youtube_icon[i].setText("")
            self.ui.linked_youtube_icon[i].setObjectName("linked_youtube_icon")
            self.ui.linked_id[i].setGeometry(QtCore.QRect(210, 80, 341, 20))
            font = QtGui.QFont()
            font.setFamily("서울남산체 M")
            font.setPointSize(9)
            self.ui.linked_id[i].setFont(font)
            self.ui.linked_id[i].setObjectName("linked_id")
            self.ui.linked_id[i].setText(downloaddata[i]['url'])
            self.ui.verticalLayout_7.addWidget(self.ui.linked_p[i])


    def add_now_list(self,downloaddata):
        length = len(downloaddata)
        self.ui.now_panel = [QtWidgets.QWidget(self.ui.now_download_layout) for i in range(length)]
    

        for i in range(length):
            self.ui.now_panel[i].setMinimumSize(QtCore.QSize(0, 120))
            self.ui.now_panel[i].setMaximumSize(QtCore.QSize(16777215, 120))
            self.ui.now_panel[i].setObjectName("now_panel")

        self.ui.now_image = [QtWidgets.QLabel(self.ui.now_panel[i]) for i in range(length)]
        self.ui.now_youtube_icon = [QtWidgets.QLabel(self.ui.now_panel[i]) for i in range(length)]
        self.ui.now_title = [QtWidgets.QLabel(self.ui.now_panel[i]) for i in range(length)]
        self.ui.now_id = [QtWidgets.QLabel(self.ui.now_panel[i]) for i in range(length)]
        self.ui.now_bar = [QtWidgets.QProgressBar(self.ui.now_panel[i]) for i in range(length)]
        for i in range(length):

            self.ui.now_image[i].setGeometry(QtCore.QRect(10, 10, 160, 90))
            self.ui.now_image[i].setStyleSheet("background-color : black ;")
            
            
            url = downloaddata[i]['thumbnail']
            tmp_data = urllib.request.urlopen(url).read()

            tmp_image = QtGui.QImage()
            tmp_image.loadFromData(tmp_data)

            self.ui.now_image[i].setPixmap(QtGui.QPixmap(tmp_image))
            self.ui.now_image[i].setScaledContents(True)
            
            self.ui.now_image[i].setObjectName("now_image")

            self.ui.now_bar[i].setGeometry(QtCore.QRect(180, 80, 431, 20))
            font = QtGui.QFont()
            font.setFamily("서울남산체 M")
            self.ui.now_bar[i].setFont(font)
            self.ui.now_bar[i].setStyleSheet("QProgressBar {\n"
    "     border: 2px solid grey;\n"
    "     border-radius: 5px;\n"
    "     background-color: #FFFFFF;\n"
    "     text-color : rgb(128,128,128);\n"
    "}\n"
    "\n"
    " QProgressBar::chunk {\n"
    "     background-color: #A293BD;\n"
    "     width: 20px;\n"
    " }")
            self.ui.now_bar[i].setProperty("value", 58)
            self.ui.now_bar[i].setAlignment(QtCore.Qt.AlignCenter)
            self.ui.now_bar[i].setObjectName("now_bar")

            self.ui.now_youtube_icon[i] = QtWidgets.QLabel(self.ui.now_panel[i])
            self.ui.now_youtube_icon[i].setGeometry(QtCore.QRect(180, 55, 21, 21))
            self.ui.now_youtube_icon[i].setStyleSheet("image:url(./image/sub1.png);")
            self.ui.now_youtube_icon[i].setText("")
            self.ui.now_youtube_icon[i].setObjectName("now_youtube_icon")

            self.ui.now_title[i] = QtWidgets.QLabel(self.ui.now_panel[i])
            self.ui.now_title[i].setGeometry(QtCore.QRect(178, 10, 421, 51))
            font = QtGui.QFont()
            font.setFamily("서울남산체 EB")
            font.setPointSize(12)
            self.ui.now_title[i].setFont(font)
            self.ui.now_title[i].setScaledContents(False)
            self.ui.now_title[i].setWordWrap(True)
            self.ui.now_title[i].setObjectName("now_title")

            ######
            self.ui.now_title[i].setText(downloaddata[i]['title'])


            self.ui.now_id[i] = QtWidgets.QLabel(self.ui.now_panel[i])
            self.ui.now_id[i].setGeometry(QtCore.QRect(208, 55, 351, 20))
            font = QtGui.QFont()
            font.setFamily("서울남산체 M")
            font.setPointSize(9)
            self.ui.now_id[i].setFont(font)
            self.ui.now_id[i].setObjectName("now_id")


            ###
            self.ui.now_id[i].setText(downloaddata[i]['url'])


            self.ui.now_image[i].raise_()
            self.ui.now_bar[i].raise_()
            self.ui.now_title[i].raise_()
            self.ui.now_id[i].raise_()
            self.ui.now_youtube_icon[i].raise_()
            self.ui.verticalLayout_6.addWidget(self.ui.now_panel[i])

        self.ui.now_bar[1].setValue(50)
    
