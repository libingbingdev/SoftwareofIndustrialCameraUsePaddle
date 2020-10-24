# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys


class Config(object):
    def __init__(self):
        # "one_camera" "two_camera" "two_camera_service"
        self.camera_mode = "None"
        # "camera_one_connect_sucess" "camera_two_connect_sucess" "camera_one_connect_failure" "camera_two_connect_failure"
        self.camera_connect_flag = "None"
        # "camera_one_open_sucess" "camera_two_open_sucess" "camera_one_open_failure" "camera_two_open_failure"
        self.camera_open_flag = "None"

class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.init() # 初始化
        self.defineConnect() # 定义界面显示逻辑用的槽函数
        self.config = Config()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1076, 591)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_choose_mode = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_choose_mode.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.pushButton_choose_mode.setObjectName("pushButton_choose_mode")
        self.pushButton_one_camera = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_one_camera.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.pushButton_one_camera.setMouseTracking(False)
        self.pushButton_one_camera.setAutoFillBackground(False)
        self.pushButton_one_camera.setAutoRepeat(False)
        self.pushButton_one_camera.setAutoExclusive(False)
        self.pushButton_one_camera.setAutoDefault(False)
        self.pushButton_one_camera.setDefault(False)
        self.pushButton_one_camera.setFlat(False)
        self.pushButton_one_camera.setObjectName("pushButton_one_camera")
        self.pushButton_two_camera_service = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_two_camera_service.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.pushButton_two_camera_service.setObjectName("pushButton_two_camera_service")
        self.pushButton_two_camera = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_two_camera.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.pushButton_two_camera.setObjectName("pushButton_two_camera")
        self.pushButton_camera_one = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_camera_one.setGeometry(QtCore.QRect(140, 30, 111, 31))
        self.pushButton_camera_one.setAutoFillBackground(False)
        self.pushButton_camera_one.setObjectName("pushButton_camera_one")
        self.pushButton_connect_camera = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_connect_camera.setGeometry(QtCore.QRect(140, 0, 111, 31))
        self.pushButton_connect_camera.setObjectName("pushButton_connect_camera")
        self.pushButton_camera_two = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_camera_two.setGeometry(QtCore.QRect(140, 60, 111, 31))
        self.pushButton_camera_two.setObjectName("pushButton_camera_two")
        self.pushButton_open_camera = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_open_camera.setGeometry(QtCore.QRect(270, 0, 111, 31))
        self.pushButton_open_camera.setObjectName("pushButton_open_camera")
        self.pushButton_start_infer = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_start_infer.setGeometry(QtCore.QRect(400, 0, 111, 31))
        self.pushButton_start_infer.setObjectName("pushButton_start_infer")
        self.pushButton_stop_infer = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_stop_infer.setGeometry(QtCore.QRect(530, 0, 111, 31))
        self.pushButton_stop_infer.setObjectName("pushButton_stop_infer")
        self.label_img_one = QtWidgets.QLabel(self.centralWidget)
        self.label_img_one.setGeometry(QtCore.QRect(10, 170, 391, 281))
        self.label_img_one.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.label_img_one.setText("")
        self.label_img_one.setObjectName("label_img_one")
        self.label_img_two = QtWidgets.QLabel(self.centralWidget)
        self.label_img_two.setGeometry(QtCore.QRect(430, 170, 391, 281))
        self.label_img_two.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.label_img_two.setText("")
        self.label_img_two.setObjectName("label_img_two")
        self.pushButton_message_one = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_message_one.setGeometry(QtCore.QRect(120, 470, 151, 41))
        self.pushButton_message_one.setObjectName("pushButton_message_one")
        self.pushButton_message_two = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_message_two.setGeometry(QtCore.QRect(540, 470, 151, 41))
        self.pushButton_message_two.setObjectName("pushButton_message_two")
        self.pushButton_choose_infer_model = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_choose_infer_model.setGeometry(QtCore.QRect(840, 210, 231, 41))
        self.pushButton_choose_infer_model.setObjectName("pushButton_choose_infer_model")
        self.pushButton_confidence_adjust = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_confidence_adjust.setGeometry(QtCore.QRect(840, 260, 231, 41))
        self.pushButton_confidence_adjust.setObjectName("pushButton_confidence_adjust")
        self.pushButton_set_pix = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_set_pix.setGeometry(QtCore.QRect(840, 310, 231, 41))
        self.pushButton_set_pix.setObjectName("pushButton_set_pix")
        self.pushButton_save_img = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_save_img.setGeometry(QtCore.QRect(840, 360, 231, 41))
        self.pushButton_save_img.setObjectName("pushButton_save_img")
        self.pushButton_usb_camera = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_usb_camera.setGeometry(QtCore.QRect(140, 90, 111, 31))
        self.pushButton_usb_camera.setObjectName("pushButton_usb_camera")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1076, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_choose_mode.setText(_translate("MainWindow", "模式选择    ▾"))
        self.pushButton_one_camera.setText(_translate("MainWindow", "单相机"))
        self.pushButton_two_camera_service.setText(_translate("MainWindow", "多相机服务"))
        self.pushButton_two_camera.setText(_translate("MainWindow", "多相机"))
        self.pushButton_camera_one.setText(_translate("MainWindow", "GIGE相机一"))
        self.pushButton_connect_camera.setText(_translate("MainWindow", "连接相机    ▾"))
        self.pushButton_camera_two.setText(_translate("MainWindow", "GIGE相机二"))
        self.pushButton_open_camera.setText(_translate("MainWindow", "打开相机"))
        self.pushButton_start_infer.setText(_translate("MainWindow", "开始预测"))
        self.pushButton_stop_infer.setText(_translate("MainWindow", "停止预测"))
        self.pushButton_message_one.setText(_translate("MainWindow", "识别信息"))
        self.pushButton_message_two.setText(_translate("MainWindow", "识别信息"))
        self.pushButton_choose_infer_model.setText(_translate("MainWindow", "模型选择与更换"))
        self.pushButton_confidence_adjust.setText(_translate("MainWindow", "置信度调节"))
        self.pushButton_set_pix.setText(_translate("MainWindow", "矩形框/像素设定"))
        self.pushButton_save_img.setText(_translate("MainWindow", "选择是否保存图片"))
        self.pushButton_usb_camera.setText(_translate("MainWindow", "USB相机"))


    def hideCombox(self,flag = 0,mode = "None"):
        if mode == "one_camera":
            self.pushButton_camera_two.setEnabled(False)
        elif "two_camera" in mode:
            self.pushButton_camera_two.setEnabled(True)

        if flag == 1:
            self.pushButton_two_camera_service.setVisible(False)
            self.pushButton_one_camera.setVisible(False)
            self.pushButton_two_camera.setVisible(False)
            self.pushButton_choose_mode.setText("模式选择    ▾")
        elif flag == 2:
            self.pushButton_camera_one.setVisible(False)
            self.pushButton_camera_two.setVisible(False)
            self.pushButton_usb_camera.setVisible(False)
            self.pushButton_connect_camera.setText("连接相机    ▾")
        elif flag == 0:
            self.pushButton_two_camera_service.setVisible(False)
            self.pushButton_one_camera.setVisible(False)
            self.pushButton_two_camera.setVisible(False)
            self.pushButton_choose_mode.setText("模式选择    ▾")
            self.pushButton_camera_one.setVisible(False)
            self.pushButton_camera_two.setVisible(False)
            self.pushButton_usb_camera.setVisible(False)
            self.pushButton_connect_camera.setText("连接相机    ▾")


    def showCombox(self,flag):
        if flag == 1:
            text = self.pushButton_choose_mode.text()
            if text == "模式选择    ▴":
                self.pushButton_two_camera_service.setVisible(False)
                self.pushButton_one_camera.setVisible(False)
                self.pushButton_two_camera.setVisible(False)
            else:
                self.pushButton_two_camera_service.setVisible(True)
                self.pushButton_one_camera.setVisible(True)
                self.pushButton_two_camera.setVisible(True)
            text = "模式选择    ▴" if text == "模式选择    ▾" else "模式选择    ▾"
            self.pushButton_choose_mode.setText(text)
        elif flag == 2:
            text = self.pushButton_connect_camera.text()
            if text == "连接相机    ▴":
                self.pushButton_camera_one.setVisible(False)
                self.pushButton_camera_two.setVisible(False)
                self.pushButton_usb_camera.setVisible(False)
            else:
                self.pushButton_camera_one.setVisible(True)
                self.pushButton_camera_two.setVisible(True)
                self.pushButton_usb_camera.setVisible(True)

            text = "连接相机    ▴" if text == "连接相机    ▾" else "连接相机    ▾"
            self.pushButton_connect_camera.setText(text)

    def init(self):
        self.hideCombox()
        self.MainWindow.setFixedSize(self.MainWindow.width(), self.MainWindow.height())

    def defineConnect(self):
        self.pushButton_choose_mode.clicked.connect(lambda: self.showCombox(1))
        self.pushButton_connect_camera.clicked.connect(lambda: self.showCombox(2))
        self.pushButton_one_camera.clicked.connect(lambda: self.hideCombox(1,"one_camera"))
        self.pushButton_two_camera.clicked.connect(lambda: self.hideCombox(1,"two_camera"))
        self.pushButton_two_camera_service.clicked.connect(lambda: self.hideCombox(1,"two_camera_service"))

        self.pushButton_camera_one.clicked.connect(lambda: self.hideCombox(2,"camera_one"))
        self.pushButton_camera_two.clicked.connect(lambda: self.hideCombox(2,"camera_two"))
        self.pushButton_usb_camera.clicked.connect(lambda: self.hideCombox(2, "camera_usb"))
