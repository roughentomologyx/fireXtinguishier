# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(985, 720, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(855, 720, 111, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1121, 711))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: white; border-width: 1px; border-color: grey; border-style: outset;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_6.setGeometry(QtCore.QRect(0, 0, 1111, 681))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1109, 679))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line.setGeometry(QtCore.QRect(0, 110, 1111, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea.setGeometry(QtCore.QRect(725, 5, 341, 101))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 321, 81))
        self.label_6.setStyleSheet("border-width: 0px;")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_5.setGeometry(QtCore.QRect(725, 480, 341, 101))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 339, 99))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 321, 81))
        self.label_11.setStyleSheet("border-width: 0px;")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_8)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_5.setGeometry(QtCore.QRect(0, 590, 1111, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_3.setGeometry(QtCore.QRect(725, 240, 341, 101))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 339, 99))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 321, 81))
        self.label_9.setStyleSheet("border-width: 0px;")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)
        self.cookies_and_site_data = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.cookies_and_site_data.setGeometry(QtCore.QRect(10, 270, 196, 31))
        self.cookies_and_site_data.setStyleSheet("border-width: 0px; font-size: 17px")
        self.cookies_and_site_data.setObjectName("checkBox_3")
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_3.setGeometry(QtCore.QRect(0, 350, 1111, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.do_not_track = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.do_not_track.setGeometry(QtCore.QRect(10, 150, 161, 31))
        self.do_not_track.setStyleSheet("border-width: 0px; font-size: 17px")
        self.do_not_track.setObjectName("do_not_track")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_4.setGeometry(QtCore.QRect(725, 360, 341, 101))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 339, 99))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 321, 81))
        self.label_10.setStyleSheet("border-width: 0px;")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_7)
        self.content_blocking = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.content_blocking.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.content_blocking.setStyleSheet("border-width: 0px; font-size: 17px")
        self.content_blocking.setObjectName("content_blocking")
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 1111, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 510, 191, 31))
        self.checkBox_5.setStyleSheet("border-width: 0px; font-size: 17px")
        self.checkBox_5.setObjectName("checkBox_5")
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_4.setGeometry(QtCore.QRect(0, 470, 1111, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_2.setGeometry(QtCore.QRect(725, 120, 341, 101))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 339, 99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 321, 81))
        self.label_8.setStyleSheet("border-width: 0px;")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 390, 161, 31))
        self.checkBox_4.setStyleSheet("border-width: 0px; font-size: 17px")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_4)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1090, 5, 21, 671))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_7.setGeometry(QtCore.QRect(210, 120, 491, 101))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 489, 99))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setGeometry(QtCore.QRect(5, 5, 476, 91))
        self.label_2.setStyleSheet("border-width: 0px;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_8 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_8.setGeometry(QtCore.QRect(210, 5, 491, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_8.sizePolicy().hasHeightForWidth())
        self.scrollArea_8.setSizePolicy(sizePolicy)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 489, 99))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_3.setGeometry(QtCore.QRect(5, 5, 476, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("border-width: 0px;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_5)
        self.scrollArea_9 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_9.setGeometry(QtCore.QRect(210, 240, 491, 101))
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 489, 99))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_4.setGeometry(QtCore.QRect(5, 5, 476, 91))
        self.label_4.setStyleSheet("border-width: 0px;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.scrollArea_10 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_10.setGeometry(QtCore.QRect(210, 360, 491, 101))
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName("scrollArea_10")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 489, 99))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_5.setGeometry(QtCore.QRect(5, 5, 476, 91))
        self.label_5.setStyleSheet("border-width: 0px;")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.scrollArea_11 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_4)
        self.scrollArea_11.setGeometry(QtCore.QRect(210, 480, 491, 101))
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setObjectName("scrollArea_11")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 489, 99))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_7.setGeometry(QtCore.QRect(5, 5, 476, 91))
        self.label_7.setStyleSheet("border-width: 0px;")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(585, 725, 231, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Apply Changes"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset to Default"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.cookies_and_site_data.setText(_translate("MainWindow", "Cookies and Site data:"))
        self.do_not_track.setText(_translate("MainWindow", "Do not Track:"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.content_blocking.setText(_translate("MainWindow", "Content Blocking: "))
        self.checkBox_5.setText(_translate("MainWindow", "Accessability Servies:"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_4.setText(_translate("MainWindow", "History:"))
        self.label_2.setText(_translate("MainWindow", "Options > Privacy & Security > Browser Privacy > Content Blocking > \n"
"4Do not Track > always\n"
"or about:settings > privacy.donottrackheader.enabled"))
        self.label_3.setText(_translate("MainWindow", "Options > Privacy & Security > Browser Privacy > Content Blocking > \n"
"4Do not Track > always\n"
"or about:settings > privacy.donottrackheader.enabled"))
        self.label_4.setText(_translate("MainWindow", "Options > Privacy & Security > Browser Privacy > Content Blocking > \n"
"4Do not Track > always\n"
"or about:settings > privacy.donottrackheader.enabled"))
        self.label_5.setText(_translate("MainWindow", "Options > Privacy & Security > Browser Privacy > Content Blocking > \n"
"4Do not Track > always\n"
"or about:settings > privacy.donottrackheader.enabled"))
        self.label_7.setText(_translate("MainWindow", "Options > Privacy & Security > Browser Privacy > Content Blocking > \n"
"4Do not Track > always\n"
"or about:settings > privacy.donottrackheader.enabled"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Firefox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Some Other App"))
