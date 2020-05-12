from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()
print(now.toString())
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())