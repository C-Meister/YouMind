import sys
from Ui_test2 import *
import urllib.request



def add_download_list(self): #함수명 알아서 바꾸셈
    length = len(downloaddata)
    ui.linked_p = [QtWidgets.QWidget(ui.layout_link_data) for i in range(length)]
   

    for i in range(length):
        ui.linked_p[i] = QtWidgets.QWidget(ui.layout_link_data)
        ui.linked_p[i].setMinimumSize(QtCore.QSize(0, 120))
        ui.linked_p[i].setMaximumSize(QtCore.QSize(16777215, 120))
        ui.linked_p[i].setObjectName("linked_p")


    ui.linked_image = [QtWidgets.QLabel(ui.linked_p[i]) for i in range(length)]
    ui.linked_title = [QtWidgets.QLabel(ui.linked_p[i]) for i in range(length)]
    ui.linked_youtube_icon = [QtWidgets.QLabel(ui.linked_p[i]) for i in range(length)]
    ui.linked_id = [QtWidgets.QLabel(ui.linked_p[i]) for i in range(length)]


    for i in range(length):  
        ui.linked_image[i].setGeometry(QtCore.QRect(10, 10, 160, 90))
        ui.linked_image[i].setStyleSheet("background-color : black ;")
        ui.linked_image[i].setObjectName("linked_image")

        url = downloaddata[i]['thumbnail']
        tmp_data = urllib.request.urlopen(url).read()

        tmp_image = QtGui.QImage()
        tmp_image.loadFromData(tmp_data)

        ui.linked_image[i].setPixmap(QtGui.QPixmap(tmp_image))


        ui.linked_title[i].setGeometry(QtCore.QRect(180, 10, 371, 71))
        ui.linked_title[i].setText(downloaddata[i]['title'])
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(16)
        ui.linked_title[i].setFont(font)
        ui.linked_title[i].setScaledContents(False)
        ui.linked_title[i].setWordWrap(True)
        ui.linked_title[i].setObjectName("linked_title")
        
        ui.linked_youtube_icon[i].setGeometry(QtCore.QRect(182, 80, 21, 21))
        ui.linked_youtube_icon[i].setStyleSheet("image:url(./image/sub1.png);")
        ui.linked_youtube_icon[i].setText("")
        ui.linked_youtube_icon[i].setObjectName("linked_youtube_icon")
        ui.linked_id[i].setGeometry(QtCore.QRect(210, 80, 351, 20))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(9)
        ui.linked_id[i].setFont(font)
        ui.linked_id[i].setObjectName("linked_id")
        ui.linked_id[i].setText(downloaddata[i]['url'])
        ui.verticalLayout_7.addWidget(ui.linked_p[i])




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

MainWindow.show()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)


#요게 데이터이고 함수로 넘겨주는게 아니여서 전역변수 씀 그래서 downloaddata명ㅇ인데 일단 ㅎㅎ
downloaddata = [
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가ssssssssssssssssfaerraerㅁ다검;ㄴ이럼ㄴ이ㅑㅈㄷ나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"},
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"}
]


add_download_list(downloaddata)

app.exec_()

