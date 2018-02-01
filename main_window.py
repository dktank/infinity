# coding:utf-8

import sys
import random
import datetime
from PyQt5 import QtWidgets as QTW
from PyQt5 import QtCore as QTC
from PyQt5 import QtGui  as QTG
"""
from PyQt5.QtWidgets import (
    QWidget, QMainWindow, QAction,
    QVBoxLayout, QLabel, QPushButton
)
"""

SRC = './resource/secret_garden.jpg'
tar = './resource/secret_garden_tmp.jpg'

import cv2, numpy, random, sys

def test():
    """
    测试函数
    :return:
    """
    print (str(datetime.datetime.now())[:19] , random.randint(1000,9999) * 1.00 / 1000)


class IFMainWindow(QTW.QMainWindow):

    def __init__(self):
        super().__init__()

        self.resize(1500, 800)
        self.move(200, 200)
        self.setWindowTitle("  infinity Research ")

        self.initMenu()
        self.initContent()

    def initMenu(self):
        """
        创建菜单
        :return:
        """

        self.statusBar().showMessage("时间飞逝")

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
        l2 = QTW.QLabel()
        btnQuit = QTW.QPushButton("一键偷蛋摸王(&C)")
        # 主qw
        self.main_qw = qw = QTW.QWidget()
        vbox = QTW.QVBoxLayout()

        vbox.addWidget(l1)
        vbox.addWidget(l2)
        vbox.addWidget(btnQuit)

        qw.setLayout(vbox)

        # 设置主qw
        self.setCentralWidget(qw)

        btnQuit.clicked.connect(self.change_l1)

        self.main_qw.l1 = l1
        self.main_qw.l2 = l2
        self.main_qw.btnQuit = btnQuit
        self.main_qw.vbox = vbox

        self.main_qw.l1.setAlignment(QTC.Qt.AlignHCenter)
        self.main_qw.l2.setAlignment(QTC.Qt.AlignHCenter)
        self.load_l2()

        self.cnt = 0

    def change_l1(self):
        """
        :return:
        """
        if self.cnt == -1:
            self.close()

        res = random.randint(1000, 9999) * 1.00 / 10000

        if res < 0.95 and self.cnt >= 0 :
            self.main_qw.l1.setText("摸蛋成功, 偷王次数: {cnt}".format(cnt=self.cnt + 1))
            self.cnt += 1
            self.redraw_l2()
        else:
            self.main_qw.l1.setText("摸蛋失败, 再摸完蛋, 已成功摸王: {cnt}次".format(cnt=self.cnt + 1))
            self.cnt = -1

    def load_l2(self):
        """
        :return:
        """
        pm = QTG.QPixmap(SRC)

        self.main_qw.l2.setPixmap(pm)


    def redraw_l2(self):
        """

        :return:
        """
        # cv2 读取文件
        original = cv2.imread(SRC)
        output = original.copy()

        # 转灰度图
        bgr2gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)  # 转灰度图

        # 二值化
        ret, threshold = cv2.threshold(bgr2gray, 170, 255, cv2.THRESH_BINARY)

        # 01化
        bitwise_not = cv2.bitwise_not(threshold)

        # 检测轮廓
        image, cnts, hierarchy = cv2.findContours(bitwise_not, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #(bitwise_not, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for cnt in cnts:
            # 上色
            color = cv2.cvtColor(numpy.uint8([[[random.randint(0, 170), random.randint(150, 250), random.randint(150, 255)]]]),
                         cv2.COLOR_HSV2BGR)[0, 0]

            cv2.drawContours(output, [cnt], 0, [int(i) for i in color], -1)

        cv2.imwrite(tar, output)

        pm = QTG.QPixmap(tar)

        self.main_qw.l2.setPixmap(pm)
