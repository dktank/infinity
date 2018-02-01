# coding:utf-8

import sys
import random
import datetime
from PyQt5 import QtWidgets as QTW
from PyQt5 import QtCore as QTC
"""
from PyQt5.QtWidgets import (
    QWidget, QMainWindow, QAction,
    QVBoxLayout, QLabel, QPushButton
)
"""


def test():
    """
    测试函数
    :return:
    """
    print (str(datetime.datetime.now())[:19] , random.randint(1000,9999) * 1.00 / 1000)


class IFMainWindow(QTW.QMainWindow):

    def __init__(self):
        super().__init__()

        self.resize(450, 300)
        self.move(200, 700)
        self.setWindowTitle("  infinity Research ")

        self.initMenu()
        self.initContent()

    def initMenu(self):
        """
        创建菜单
        :return:
        """

        self.statusBar().showMessage("+1s")

        # 创建菜单
        menu = self.menuBar()
        # 创建子菜单
        file_menu = menu.addMenu('文件')
        #file_menu.addSeparator()
        edit_menu = menu.addMenu('修改')

        #exit_menu = menu.addMenu('退出')

        # 新文件
        new_action = QTW.QAction('新文件', self)#.setStatusTip("新的文件")
        new_action.setStatusTip("新的文件")
        file_menu.addAction(new_action)
        #new_action.triggered.connect(test)

        exit_action = QTW.QAction('退出', self)
        exit_action.setStatusTip('点击退出')
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)

    def initContent(self):
        """

        :return:
        """


        l1 = QTW.QLabel("hello world! ")
        btnQuit = QTW.QPushButton("一键偷蛋摸王(&C)")
        self.main_qw = qw = QTW.QWidget()
        vbox = QTW.QVBoxLayout()

        vbox.addWidget(l1)
        vbox.addWidget(btnQuit)

        qw.setLayout(vbox)
        self.setCentralWidget(qw)

        btnQuit.clicked.connect(self.close)

        self.main_qw.l1 = l1
        self.main_qw.btnQuit = btnQuit
        self.main_qw.vbox = vbox

        self.main_qw.l1.setAlignment(QTC.Qt.AlignHCenter)

