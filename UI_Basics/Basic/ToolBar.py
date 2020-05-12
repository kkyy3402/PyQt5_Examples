import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #닫는 액션1
        exitAction = QAction(QIcon('web.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        # 스테이터스 바에 설명을 추가한다.
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        #닫는 액션2
        exitAction2 = QAction(QIcon('web.png'), 'Exit', self)
        exitAction2.setShortcut('Ctrl+Q')
        #스테이터스 바에 설명을 추가한다.
        exitAction2.setStatusTip('Exit application')
        exitAction2.triggered.connect(qApp.quit)

        #statusBar를 쓸수 있게 activate 시킨다.
        self.statusBar()

        #툴바 한줄을 추가한다.
        self.toolbar = self.addToolBar('Exit')

        #툴바에 액션이 담긴 아이콘을 추가한다.
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(exitAction2)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())