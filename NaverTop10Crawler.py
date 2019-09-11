import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
from bs4 import BeautifulSoup


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeScreen()

    def initializeScreen(self):
        # 위젯들을 그리드 layout에 집어넣을 예정입니다.
        grid = QGridLayout()
        self.setLayout(grid)

        # 타이틀 텍스트를 선언합니다.
        self.titleLabel = QLabel("크롤링 예제")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFixedHeight(50)
        self.titleLabel.setFont(QFont("Ubuntu", pointSize=15, weight=QFont.Bold))

        self.startCrawlingBtn = QPushButton("크롤링 시작")
        self.startCrawlingBtn.clicked.connect(self.getTop10FromNaver)

        self.rankListView = RankListView()

        # 타이틀 및 화면 왼쪽에 있는 위젯들을 등록합니다.
        grid.addWidget(self.titleLabel, 0, 0)
        grid.addWidget(self.startCrawlingBtn, 1, 0)
        grid.addWidget(RankListView(), 2, 0)

        self.setWindowTitle("네이버 탑 10 크롤러")
        self.windowToCenter()
        self.show()

    # 창을 가운데로 이동시키는 메서드입니다.
    def windowToCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getTop10FromNaver(self):

        ranks = []
        keywords = []

        print("Crawling...")
        res = requests.get("https://naver.com")

        # 성공!
        if res.status_code == 200:

            dom = BeautifulSoup(res.text, "html.parser")
            elements = dom.select(
                '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul')

            for idx, element in enumerate(elements[0]):
                if type(element).__name__ == "Tag":
                    # print("idx : {} , element : {}".format(idx,element))

                    rank = element.select(".ah_r")[0].text
                    keyword = element.select(".ah_k")[0].text

                    ranks.append(rank)
                    keywords.append(keyword)

                    print("rank : {}, keyword : {}".format(rank, keyword))

            self.rankListView.setData(keywords)

        else:
            print("failed!")
            # 실패


class RankListView(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("ItemView QListView")
        self.setFixedHeight(100)

        self.view = QListView(self)
        self.model = QStandardItemModel()

    def setData(self, items):
        print(items)

        for item in items:
            print(item)
            self.model.appendRow(QStandardItem(item))

        # for item in items:
        # self.model.appendRow(QStandardItem(item))
        self.model.dataChanged

        self.view.setModel(self.model)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    sys.exit(app.exec_())
