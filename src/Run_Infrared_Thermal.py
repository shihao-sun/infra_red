#! /usr/local/lib/python3.6
#encoding:utf-8
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import os
from PyQt5.QtCore import Qt

from Infrared_Thermal import Ui_MainWindow
class IMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(IMainWindow, self).__init__()
        self.setupUi(self)
        self.Button_Quit.clicked.connect(lambda:self.close())
        self.Button_NextPic.clicked.connect(lambda :self.nextPic())
        self.Button_PrePic.clicked.connect(lambda: self.prePic())
        self.Button_ShotBegin.clicked.connect(lambda: self.display())
        self.ImFolder = ''  # 图片文件夹路径
        self.ImNameSet = []  # 图片集合
        self.CurImId = 0  # 当前显示图在集合中的编号
        self.ImLen=len(self.ImNameSet)


        self.ImFolder = './imag'
        self.ImNameSet = os.listdir(self.ImFolder)
        self.ImNameSet.sort()
    def display(self):
        if self.ImFolder != '':
            ImFolder=self.ImFolder
            ImNameSet = self.ImNameSet
            ImPath = os.path.join(ImFolder, ImNameSet[0])
            pix = QPixmap(ImPath)
            self.label.setPixmap(pix)
            self.label.resize(784, 500)
            self.label.move(50, 100)

    def nextPic(self):
        ImFolder = self.ImFolder
        ImNameSet = self.ImNameSet
        CurImId = self.CurImId
        ImNum = len(ImNameSet)
        if CurImId < ImNum - 1:  # 不可循环看图
            ImPath = os.path.join(ImFolder, ImNameSet[CurImId + 1])
            pix = QPixmap(ImPath)
            self.label.setPixmap(pix)
            self.CurImId = CurImId + 1

    def prePic(self):
         ImFolder = self.ImFolder
         ImNameSet = self.ImNameSet
         CurImId = self.CurImId
         ImNum = len(ImNameSet)
         if CurImId > 0:  # 第一张图片没有前一张
            ImPath = os.path.join(ImFolder, ImNameSet[CurImId - 1])
            pix = QPixmap(ImPath)
            self.label.setPixmap(pix)
            self.CurImId = CurImId - 1


"""
    def next(self):
        self.img2=QPixmap('icon_shot.png')
        self.label.setPixmap(img2)
        self.label.resize(784,500)
        self.label.move(50,100)





    def printEvent(self,event):
        super().paintEvent(event)
        pt=QPainter()
        pt.begin()
        img=QImage('icon_camera.jpg')
        rect= QRect(60,80,30,40)
        pt.drawImage(rect,img)
        pt.end()
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = IMainWindow()
    w.show()
    sys.exit(app.exec_())
