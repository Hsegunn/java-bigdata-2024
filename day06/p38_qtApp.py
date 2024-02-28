# file: p38_qtApp.py
# desc: PyQt5 앱 만들기 (이어서)

''' 
설치 > pip install PyQt5 
시그널 == 이벤트, 위젯 == 컨트롤
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import * 

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__()  
        self.initUI()

    def initUI(self):
        self.setGeometry((1920-300)//2, (1080-300)//2, 320, 230) # 해상도 1920x1080에서 정중앙에 위치
        self.setWindowTitle('세번째 QT앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 화면 UI에서 추가/변경할 것
        btn1 = QPushButton('클릭',self)
        btn1.setGeometry(210,180,100,40)
        btn1.clicked.connect(self.btn1Clicked) # 버튼클릭 시그널이 발생하면 이를 처리하는 함수 연결

        self.show()
    
    def btn1Clicked(self):
        QMessageBox.about(self, '알림창', '버튼이 눌렸습니다')

    def closeEvent(self, QCloseEvent) -> None: # 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes: # 창 닫기
            QCloseEvent.accept() 
        else: # 창 유지
            QCloseEvent.ignore()

app = QApplication(sys.argv) 
inst = qtApp() 
app.exec_() 
