from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
import pyperclip

import threading

class Btn(QtWidgets.QMainWindow):
    def btn_add(self,list1, yt):
        self.list1 = list1
        self.yt = yt

    def btn_link_event(self):

        url = pyperclip.paste()

        self.list1.add_download_list(self.yt.get_videos(url))









        
        # message = "<font size = 5 color = gray > Rich Html Title </font> <br/><br/>The clickable link <a href='http://www.google.com'>Google.</a> The lower and upper case text."
        # messagebox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "title", message, parent=self)
        # messagebox.addButton("1", QtWidgets.QMessageBox.ResetRole)
        # messagebox.addButton("2", QtWidgets.QMessageBox.ApplyRole)
        # messagebox.addButton("3", QtWidgets.QMessageBox.RejectRole)
        # exe = messagebox.exec_()
        # print('exe: %s  clickedButton: %s'%(exe, messagebox.clickedButton()))
        # print('test')
    
    def btn_sub_event(self):
        pass
    
    def Th(self):
        url_list= self.list1.urlbuf
        ext = 'mp4'
        resl = '480x360'



        self.yt.round_robin_download(url_list,ext,resl)
    
    def btn_download_event(self):
        t=threading.Thread(target=self.Th,daemon=True)
        t.start()

    def btn_file_chooser_event(self):
        pass


    def __init__(self,MainWindow):
        super().__init__()

        self.MainWindow = MainWindow 
        MainWindow.btn_link_event = self.btn_link_event
        MainWindow.btn_sub_event = self.btn_sub_event
        MainWindow.btn_download_event = self.btn_download_event
        MainWindow.btn_file_chooser_event = self.btn_file_chooser_event


    
    


    