from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QGridLayout()
        self.setLayout(grid)

        self.setWindowTitle("멀티 스레드 예제")

        self.startGetDataBtn = QPushButton()
        self.startGetDataBtn.setText("크롤링 시작하기")
        self.startGetDataBtn.clicked.connect(self.onGetDataBtnClicked)

        grid.addWidget(self.startGetDataBtn,0,0)

        self.th = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.th)
        self.worker.getDatacompleted.connect(self.onGetDataCompleted)


        self.setGeometry(100, 50, 300, 300)
        self.windowToCenter()
        self.show()

    @pyqtSlot()
    def onGetDataBtnClicked(self):
        print("Start Thread")
        self.worker.run()
        self.th.working = True

    # 창을 가운데로 이동시키는 메서드입니다.
    def windowToCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot(int)
    def onGetDataCompleted(self,data):
        print("onGetDataCompleted. data : ".format(data))

class Worker(QObject):
    getDatacompleted = pyqtSignal(int)
    data = "Hi"

    def __init__(self, parent=None):
        super().__init__()
        print("Itit")
        self.parent = parent
        self.working = True

    def __del__(self):
        print(".... end thread.....")
        self.wait()

    def run(self):
        print("Thread run!")
        data = {"foo":"bar"}
        print("self.data : {}".format(self.data))
        self.getDatacompleted.emit(1)
        self.working = False

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MainWindow()
    app.exec_()