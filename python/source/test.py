import sys
from Ui_test2 import *

from kit_class import *
from btn_class import *



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
btn = Btn(MainWindow)

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
{"thumbnail": "https://i.ytimg.com/vi/fSOpiZo1BAA/mqdefault.jpg", "url": "https://www.youtube.com/watch?v=P9J87Bxdtg8", "title" : "가나다"}
]

list1 = Kit(ui)
list1.add_now_list(downloaddata)

app.exec_()

