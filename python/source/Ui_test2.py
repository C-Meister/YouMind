# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\You_Mind\python\source\test2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 721)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 721))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 721))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(74, 0, 561, 721))
        self.stackedWidget.setMinimumSize(QtCore.QSize(441, 721))
        self.stackedWidget.setStyleSheet("background-color : rgb(242,242,242);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_link = QtWidgets.QWidget()
        self.page_link.setObjectName("page_link")
        self.btn_link_download = QtWidgets.QPushButton(self.page_link)
        self.btn_link_download.setGeometry(QtCore.QRect(380, 680, 171, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(12)
        self.btn_link_download.setFont(font)
        self.btn_link_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_link_download.setStyleSheet("QPushButton{border:0px; background-color : #A293BD; color : #FFFFFF}\n"
"QPushButton:hover{border:0px;background-color : #705697; color : #FFFFFF}")
        self.btn_link_download.setObjectName("btn_link_download")
        self.combo_link_format = QtWidgets.QComboBox(self.page_link)
        self.combo_link_format.setGeometry(QtCore.QRect(10, 680, 176, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(11)
        self.combo_link_format.setFont(font)
        self.combo_link_format.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color : #ffffff;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"\n"
"    background: #A293BD\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"            background: #705697 \n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./image/down.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.combo_link_format.setObjectName("combo_link_format")
        self.combo_link_format.addItem("")
        self.combo_link_format.addItem("")
        self.combo_link_format.addItem("")
        self.btn_link_file = QtWidgets.QPushButton(self.page_link)
        self.btn_link_file.setGeometry(QtCore.QRect(520, 640, 31, 31))
        self.btn_link_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_link_file.setStyleSheet("QPushButton{image:url(./image/folder1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/folder2.png); border:0px;background-color : rgba(0,0,0,0);}")
        self.btn_link_file.setText("")
        self.btn_link_file.setObjectName("btn_link_file")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_link)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 640, 501, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color : white; border:0px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.combo_link_format_2 = QtWidgets.QComboBox(self.page_link)
        self.combo_link_format_2.setGeometry(QtCore.QRect(200, 680, 171, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(11)
        self.combo_link_format_2.setFont(font)
        self.combo_link_format_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"\n"
"    background: #A293BD\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"            background: #705697 \n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./image/down.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.combo_link_format_2.setObjectName("combo_link_format_2")
        self.combo_link_format_2.addItem("")
        self.combo_link_format_2.addItem("")
        self.combo_link_format_2.addItem("")
        self.panel_link = QtWidgets.QScrollArea(self.page_link)
        self.panel_link.setGeometry(QtCore.QRect(0, 50, 551, 581))
        self.panel_link.setStyleSheet("border : 0px;")
        self.panel_link.setWidgetResizable(True)
        self.panel_link.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.panel_link.setObjectName("panel_link")
        self.layout_link_data = QtWidgets.QWidget()
        self.layout_link_data.setGeometry(QtCore.QRect(0, 0, 551, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layout_link_data.sizePolicy().hasHeightForWidth())
        self.layout_link_data.setSizePolicy(sizePolicy)
        self.layout_link_data.setObjectName("layout_link_data")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layout_link_data)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.panel_link.setWidget(self.layout_link_data)
        self.label_5 = QtWidgets.QLabel(self.page_link)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 571, 51))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color : rgb(255,255,255); \n"
"background-color : rgb(210,210,210);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_link)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 561, 51))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color : rgb(255,255,255); \n"
"background-color : rgb(210,210,210);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        self.pushButton.setGeometry(QtCore.QRect(220, 160, 91, 81))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{image:url(./image/add1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/add2.png); border:0px;background-color : rgba(0,0,0,0);}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.page_3)
        self.widget.setGeometry(QtCore.QRect(-10, 50, 581, 101))
        self.widget.setStyleSheet("background-color : rgb(230,230,230);")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(110, 60, 451, 31))
        font = QtGui.QFont()
        font.setFamily("서울남산체 M")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color : rgb(230,230,230);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 80, 80))
        self.label.setStyleSheet("image:url(./image/soohan.png); background-color : rgb(230,230,230);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 451, 41))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color : rgb(230,230,230);")
        self.label_2.setObjectName("label_2")
        self.widget.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.widget_17 = QtWidgets.QWidget(self.centralwidget)
        self.widget_17.setGeometry(QtCore.QRect(0, 0, 71, 721))
        self.widget_17.setStyleSheet("background-color(237,237,245);")
        self.widget_17.setObjectName("widget_17")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_17)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 71, 711))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_link = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_link.sizePolicy().hasHeightForWidth())
        self.btn_link.setSizePolicy(sizePolicy)
        self.btn_link.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_link.setStyleSheet("QPushButton{image:url(./image/link1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/link2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/link2.png); border:0px;background-color : rgba(0,0,0,0);}")
        self.btn_link.setText("")
        self.btn_link.setCheckable(True)
        self.btn_link.setChecked(False)
        self.btn_link.setObjectName("btn_link")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_link)
        self.verticalLayout_2.addWidget(self.btn_link)
        self.btn_sub = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_sub.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_sub.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sub.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_sub.setStyleSheet("QPushButton{image:url(./image/sub1.png); border:0px; background-color : rgba(0,0,0,0);}\n"
"QPushButton:hover{image:url(./image/sub2.png); border:0px;background-color : rgba(0,0,0,0);}\n"
"QPushButton:checked{image:url(./image/sub2.png); border:0px;background-color : rgba(0,0,0,0);}")
        self.btn_sub.setText("")
        self.btn_sub.setCheckable(True)
        self.btn_sub.setObjectName("btn_sub")
        self.buttonGroup.addButton(self.btn_sub)
        self.verticalLayout_2.addWidget(self.btn_sub)
        self.widget_18 = QtWidgets.QWidget(self.centralwidget)
        self.widget_18.setGeometry(QtCore.QRect(639, -1, 641, 721))
        self.widget_18.setStyleSheet("background-color : rgb(245,245,245);")
        self.widget_18.setObjectName("widget_18")
        self.now_download_scroll = QtWidgets.QScrollArea(self.widget_18)
        self.now_download_scroll.setGeometry(QtCore.QRect(0, 60, 641, 651))
        self.now_download_scroll.setStyleSheet("border : 0px")
        self.now_download_scroll.setWidgetResizable(True)
        self.now_download_scroll.setObjectName("now_download_scroll")
        self.now_download_layout = QtWidgets.QWidget()
        self.now_download_layout.setGeometry(QtCore.QRect(0, 0, 641, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.now_download_layout.sizePolicy().hasHeightForWidth())
        self.now_download_layout.setSizePolicy(sizePolicy)
        self.now_download_layout.setObjectName("now_download_layout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.now_download_layout)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.now_download_scroll.setWidget(self.now_download_layout)
        self.label_6 = QtWidgets.QLabel(self.widget_18)
        self.label_6.setGeometry(QtCore.QRect(0, 1, 641, 51))
        font = QtGui.QFont()
        font.setFamily("서울남산체 EB")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color : rgb(255,255,255); \n"
"background-color : rgb(210,210,210);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_link.clicked.connect(MainWindow.btn_link_event)
        self.btn_sub.clicked.connect(MainWindow.btn_sub_event)
        self.btn_link_file.clicked.connect(MainWindow.btn_file_chooser_event)
        self.btn_link_download.clicked.connect(MainWindow.btn_download_event)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "You_Mind | 유튜브 다운로더"))
        self.btn_link_download.setText(_translate("MainWindow", "다운로드"))
        self.combo_link_format.setItemText(0, _translate("MainWindow", "480p"))
        self.combo_link_format.setItemText(1, _translate("MainWindow", "720p"))
        self.combo_link_format.setItemText(2, _translate("MainWindow", "1080p"))
        self.combo_link_format_2.setItemText(0, _translate("MainWindow", "mp4"))
        self.combo_link_format_2.setItemText(1, _translate("MainWindow", "mp3"))
        self.combo_link_format_2.setItemText(2, _translate("MainWindow", "mkv"))
        self.label_5.setText(_translate("MainWindow", "다운로드"))
        self.label_4.setText(_translate("MainWindow", "구독"))
        self.label_3.setText(_translate("MainWindow", "구독자 23명"))
        self.label_2.setText(_translate("MainWindow", "배수한"))
        self.label_6.setText(_translate("MainWindow", "진행상황"))

