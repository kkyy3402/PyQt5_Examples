import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip,QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #창 타이틀 설정
        self.setWindowTitle('My First Application')
        #self.move(300, 300)
        #self.resize(400, 200)

        #아이콘 설정
        self.setWindowIcon(QIcon('web.png'))

        #창의 위치 및 크기를 한번에 정할 수 있다.
        self.setGeometry(300,300,300,200)

        #닫기 버튼 생성
        btn = QPushButton('닫기', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        #윈도우에 툴팁 생성
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 버튼에 툴팁 생성
        btn.setToolTip("This is Button!")

        #창을 가운데로 이동시키는
        self.center()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())