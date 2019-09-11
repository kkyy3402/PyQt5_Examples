import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeScreen()

    def initializeScreen(self):
        # 위젯들을 그리드 layout에 집어넣을 예정입니다.
        grid = QGridLayout()
        self.setLayout(grid)

        # 타이틀 텍스트를 선언합니다.
        self.titleLabel = QLabel("Login Form")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFixedHeight(50)
        self.titleLabel.setFont(QFont("Ubuntu",pointSize=15,weight=QFont.Bold))

        # 화면 왼쪽에 있는 항목들을 선언합니다.
        self.idLabel = QLabel("ID")
        self.pwLabel = QLabel("PW")
        self.pwConfirmLabel = QLabel("PW Confirm")
        self.dcLabel = QLabel("Description")

        # 화면 왼쪽에 있는 항목들의 속성을 set합니다. (가운데 정렬)
        self.idLabel.setAlignment(Qt.AlignCenter)
        self.pwLabel.setAlignment(Qt.AlignCenter)
        self.pwConfirmLabel.setAlignment(Qt.AlignCenter)
        self.dcLabel.setAlignment(Qt.AlignCenter)

        # 타이틀 및 화면 왼쪽에 있는 위젯들을 등록합니다.
        grid.addWidget(self.titleLabel,0,0,1,2)
        grid.addWidget(self.idLabel,1,0)
        grid.addWidget(self.pwLabel, 2, 0)
        grid.addWidget(self.pwConfirmLabel, 3, 0)
        grid.addWidget(self.dcLabel, 4, 0)

        # 화면 오른쪽에 있는 위젯들을 선언합니다.
        self.lineTextForID = QLineEdit()
        self.lineTextForPW = QLineEdit()
        self.lineTextForPWConfirm = QLineEdit()
        self.textEditForDC = QTextEdit()

        # 비밀번호 칸은 아래와 같이 처리하면 됩니다.
        self.lineTextForPW.setEchoMode(QLineEdit.Password)
        self.lineTextForPWConfirm.setEchoMode(QLineEdit.Password)

        # 오른쪽에 있는 위젯들을 등록합니다.
        grid.addWidget(self.lineTextForID, 1, 1)
        grid.addWidget(self.lineTextForPW, 2, 1)
        grid.addWidget(self.lineTextForPWConfirm, 3, 1)
        grid.addWidget(self.textEditForDC, 4, 1)

        # 확인 버튼을 선언하고, 이벤트 핸들러를 지정합니다.
        self.confirmBtn = QPushButton()
        self.confirmBtn.setText("Agree")
        self.confirmBtn.clicked.connect(self.onCheckFormContent)
        self.confirmBtn.setFixedHeight(50)

        # 행 , 열, from, to 순으로 arg를 집어넣으면 된다.
        grid.addWidget(self.confirmBtn, 5, 0, 1, 2)

        self.setWindowTitle("로그인")
        self.windowToCenter()
        self.show()

    #아이디 유효성 검사
    def onCheckFormContent(self):
        if self.lineTextForID.text() == "" :
            QMessageBox.question(self,"경고","아이디를 입력해주세요", QMessageBox.Yes)
            return

        if self.lineTextForPW.text() == "" :
            QMessageBox.question(self,"경고","비밀번호를 입력해주세요", QMessageBox.Yes)
            return

        if self.lineTextForPW.text() != self.lineTextForPWConfirm.text() :
            QMessageBox.question(self,"경고","비밀번호가 다릅니다.", QMessageBox.Yes)
            return

        # 메시지 박스의 확인 버튼에 이벤트 핸들러는 다음과 같이 넣을 수 있습니다.
        msg = QMessageBox()
        msg.setWindowTitle("감사합니다. ")
        msg.setText("회원가입이 완료되었습니다.")
        msg.buttonClicked.connect(self.closeWindow)
        msg.exec_()

    # 창을 가운데로 이동시키는 메서드입니다.
    def windowToCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 창을 닫는 메서드입니다.
    def closeWindow(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    sys.exit(app.exec_())