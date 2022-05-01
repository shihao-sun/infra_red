import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QDesktopWidget,QPushButton,QHBoxLayout,QWidget
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
     super(FirstMainWin,self).__init__(parent)
     self.setWindowTitle('第一个窗口')
     self.resize(400,300)
     self.status= self.statusBar()
     self.status.showMessage('只存在五秒',5000)
     self.button1=QPushButton()
     self.button1.setText('关闭程序')
     self.button1.clicked.connect(lambda :self.onCliced_Button())

     layout=QHBoxLayout()
     layout.addWidget(self.button1)

     mainFram=QWidget()
     mainFram.setLayout(layout)
     self.setCentralWidget(mainFram)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newleft = (screen.width()-size.width())/2
        nwetop = (screen.height()-size.height())/2
        self.move(newleft,nwetop)


    def onCliced_Button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        app = QApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())

