import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from Ui_test2 import *
from kit_class import *
from btn_class import *
from youtube import *
import threading
import nativemessaging

downloaddata = []
API_KEY = "AIzaSyAasuN7ChDi_8Hemxv1Dd9-troI6-Fe-7M"


class Signal(QObject):
    signal = pyqtSignal(str)

    @pyqtSlot(str)
    def onMessaged(self, message):
        print(message)
        list1.add_download_list(yt.get_videos(message))
        MainWindow.show()


def th():
    while True:
        message = nativemessaging.get_message()
        signal.signal.emit(message)
        MainWindow.setWindowState(MainWindow.windowState(
        ) & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
        MainWindow.activateWindow()


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
    signal = Signal()
    signal.signal.connect(signal.onMessaged)
    # signal.signal.emit("https://www.youtube.com/watch?v=pQAaTEItkB0")
    # list1.add_download_list(yt.get_videos('https://www.youtube.com/channel/UCMRdlwfhLECvQw0FN0s_csg'))
    btn.btn_add(list1, yt,ui)
    chromeThread = threading.Thread(target=th, daemon=True)
    chromeThread.start()
    app.exec_()
