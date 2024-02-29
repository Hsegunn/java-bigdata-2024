# file: p45_threadApp.py
# desc: PyQt5 스레드 학습용

''' 
설치 > pip install PyQt5 
설치 > pip install PyQt5Designer
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

class BackgroundWorker(QThread): # PyQt용 스레드
    initUiSignal = pyqtSignal(int) # 스레드 진행 시 UI에서 초기화 처리할 초기화 부분 시그널 전달
    setPgbSignal = pyqtSignal(int) # 스레드 진행 시 변경되는 숫자를 UI로 전달
    setTxbSignal = pyqtSignal(str) # 스레드 진행 시 화면에 출력될 문자열을 UI쪽으로 전달
    
    def __init__(self, parent) -> None: # 부모는 qtApp 클래스
        super().__init__(parent)
        self.parent = parent 

    def run(self) -> None:
        maxVal = 1_000_000
        self.initUiSignal.emit(maxVal) # 나는 값을 보내니 UI쪽(qtApp)에서 받아서 처리해줘

        for i in range(maxVal):
            print(f'스레드 진행 > {i}')
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'스레드 진행 > {i}')

            # self.parent.pgbTask.setValue(i) # UI 스레드의 권한을 백그라운드 스레드에 주지않음
            # self.parent.txbLog.append(f'스레드 진행 > {i}') # 사용불가

        

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__()  
        self.initUI()

    def initUI(self): # ui파일을 로드해서 화면디자인 사용
        uic.loadUi('./day07/testThread.ui', self)
        self.setWindowTitle('스레드 앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일 내 위젯은 자동완성 X

        self.show()

    def btnStartClicked(self):
        self.btnStart.setDisabled(True)
        th = BackgroundWorker(self) # qtApp가 부모클래스
        th.start() # 스레드 내 run() 함수 실행
        th.initUiSignal.connect(self.initPgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbLog)
        self.btnStart.setEnabled(True)

    @pyqtSlot(str) # pyqtSingal에서 넘어온 값을 처리해주는 부분이라고 선언
    def setTxbLog(self, msg):
        self.txbLog.append(msg)

    @pyqtSlot(int) # pyqtSingal에서 넘어온 값을 처리해주는 부분이라고 선언
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

    @pyqtSlot(int) # pyqtSingal에서 넘어온 값을 처리해주는 부분이라고 선언
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0,maxVal-1)



    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:
            QCloseEvent.accept() 
        else: # 창 유지
            QCloseEvent.ignore()

app = QApplication(sys.argv) 
inst = qtApp() 
app.exec_() 
