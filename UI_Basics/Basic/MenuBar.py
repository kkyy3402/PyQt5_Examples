import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('web.png'), '나가기', self)
        #단축키 설정
        exitAction.setShortcut('Ctrl+Q')
        #툴팁 설정
        exitAction.setStatusTip('화면을 나가는 것입니다.')
        #이벤트 설정
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        #윈도우의 메뉴 바 인스턴스를 가져오고
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('파일')

        #아래처럼 구현하면 Alt+F 눌렀을때 메뉴 눌러진다.
        #fileMenu = menubar.addMenu('&File')

        #메뉴에 닫기 액션을 추가해준다.
        fileMenu.addAction(exitAction)

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())