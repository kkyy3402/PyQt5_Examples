import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
from bs4 import BeautifulSoup

class NaverTop20Crawler(QWidget):

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
        self.startCrawlingBtn.clicked.connect(self.getTop20KeywordFromNaver)

        # 데이터를 뿌려줄 ListView입니다.
        self.rankListView = NaverTop20RankListView()

        # 타이틀 및 화면 왼쪽에 있는 위젯들을 등록합니다.
        grid.addWidget(self.titleLabel, 0, 0)
        grid.addWidget(self.startCrawlingBtn, 1, 0)
        grid.addWidget(self.rankListView, 2, 0)

        self.setWindowTitle("네이버 탑 20 크롤러")
        self.setFixedWidth(500)

        self.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.show()

    # 네이버에서 검색어 순위 20위까지 가져오는 함수입니다.
    # 원래 멀티스레드로 백그라운드로 돌아가게 구현해야 정석이겠져? 금방 가져오니까 일단은 메인스레드에서 작업합니당.
    def getTop20KeywordFromNaver(self):

        keywords = []
        res = requests.get("https://naver.com")
        # http response code가 200인 경우에 데이터 세팅해줍니다.
        if res.status_code == 200:

            dom = BeautifulSoup(res.text, "html.parser")
            # selector를 좀더 간단하게 할 수 있을거 같은데, 찾기 귀찮네요?
            elements = dom.select(
                '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul')

            for idx, element in enumerate(elements[0]):
                if type(element).__name__ == "Tag":
                    keyword = element.select(".ah_k")[0].text
                    keywords.append(keyword)

            self.rankListView.setData(keywords)

        # 데이터 로드에 실패하면 실패를 테이블에 뿌려줍니당.
        else:
            self.rankListView.setData(["데이터를 가져오는데 실패하였습니다."])
            # 실패


#랭킹 리스트 뷰 클래스
class NaverTop20RankListView(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setFixedHeight(650)
        self.tableWidget = QTableWidget(self)

        # 꽉 차게 대강 사이즈 맞췄습니다.
        self.tableWidget.resize(500, 650)

        # 네이버 인기검색어가 20개니까 가로 20 줄 세팅
        self.tableWidget.setRowCount(20)

        # 네이버 인기검색어가 세로 1줄
        self.tableWidget.setColumnCount(1)

        # 이걸 쳐줘야 한 셀이 한 행에 꽉 찹니다.
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def setData(self, keywords):

        self.keywords = keywords

        for idx in range(0,20):
            # 테이블 위젯에 값을 세팅해줍니다.
            item = QTableWidgetItem()
            item.setText(keywords[idx])
            item.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(idx, 0, item)

        # 셀이 클릭되었을 때 cellClicked라는 시그널이 발생하고, onCellClicked slot에 연결해준다.
        self.tableWidget.cellClicked.connect(self.onCellClicked)

    def onCellClicked(self,row,col):
        print("Selected Keyword :" ,self.keywords[row])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NaverTop20Crawler()
    sys.exit(app.exec_())
