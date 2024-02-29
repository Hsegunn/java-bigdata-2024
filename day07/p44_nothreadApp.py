# file: p44_nothreadApp.py
# desc: 스레드 학습하기

''' 
설치 > pip install PyQt5 
설치 > pip install PyQt5Designer
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__()  
        self.initUI()

    def initUI(self): # ui파일을 로드해서 화면디자인 사용
        uic.loadUi('./day07/testThread.ui', self)
        self.setWindowTitle('노스레드 앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일 내 위젯은 자동완성 X

        self.show()

    def btnStartClicked(self):
        self.pgbTask.setValue(0) # 재설정
        self.pgbTask.setRange(0,999_999) # 프로그래스바 범위 설정
        self.btnStart.setDisabled(True)
        # UI(메인) 스레드가 화면을 그릴 수 있는 여유가 없음
        for i in range(0,1_000_000): # 0~99까지
            print(f'노스레드 진행 > {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'노스레드 진행 > {i}')
        self.btnStart.setEnabled(True)
    
    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:
            QCloseEvent.accept() 
        else: # 창 유지
            QCloseEvent.ignore()

app = QApplication(sys.argv) 
inst = qtApp() 
app.exec_() 
