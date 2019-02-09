import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from Ui_test2 import *
from kit_class import *
from btn_class import *
from youtube import *
from os.path import expanduser
import threading
import nativemessaging

downloaddata = []
API_KEY = "AIzaSyBSinrqSaEr4BjZnWhbqv4fEKphbs9x0oM"


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
        # MainWindow.setWindowState(MainWindow.windowState(
        # ) & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
        # MainWindow.activateWindow()

# def get_real_resl(idx, exttype):
# 	if exttype == VIDEO:
# 		return video_resls_map[idx]
# 	else:
# 		return audio_resls_map[idx]


# def get_exttype(idx):
# 	if combo_1_items[idx] in video_formats:
# 		return VIDEO
# 	else:
# 		return AUDIO
if __name__ == "__main__":
    # VIDEO = 1
    # AUDIO = 0

    # video_formats = ['MP4 - 동영상','FLV - 동영상','MKV - 동영상','3GP - 동영상']
    # audio_formats = ['MP3 - 오디오','M4A - 오디오', 'OGG - 오디오']

    # combo_1_items = video_formats+audio_formats

    # video_resls = ['원본','1080p','720p','480p','360p','240p']
    # video_resls_map = [None,'1080','720','480','360','240']
    # audio_resls = ['원본','320kbps','256kbps','128kbps']
    # audio_resls_map = [None,'320','256','128']

    # combo_2_items = video_resls

    list1 = 0

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    defaultDir = expanduser("~") + "\\Videos"
    defaultDir = defaultDir.replace("\\", "/") + '/'
    yt = youtube(API_KEY, "")
    btn = Btn(MainWindow)
    MainWindow.show()
    ui = Ui_MainWindow()
    # ui.combo_link_format.setaddItems()
    ui.setupUi(MainWindow)
    ui.lineEdit_2.setText(defaultDir)
    list1 = Kit(ui)
    signal = Signal()
    signal.signal.connect(signal.onMessaged)
    # signal.signal.emit("https://www.youtube.com/watch?v=pQAaTEItkB0")
    # list1.add_download_list(yt.get_videos('https://www.youtube.com/channel/UCMRdlwfhLECvQw0FN0s_csg'))
    btn.btn_add(list1, yt, ui)
    chromeThread = threading.Thread(target=th, daemon=True)
    chromeThread.start()
    app.exec_()
