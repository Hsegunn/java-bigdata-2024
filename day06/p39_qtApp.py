# file: p39_qtApp.py
# desc: PyQt5, QtDesinger를 같이 사용

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
        uic.loadUi('./day06/firstApp.ui', self)
        
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnMsg.clicked.connect(self.btnMsgClicked) # ui 파일 내 위젯은 자동완성 X

        self.show()

    def btnMsgClicked(self):
        QMessageBox.about(self, 'Qt디자이너', '클릭하였습니다')
        self.label.setText('What the hell')
    
    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:
            QCloseEvent.accept() 
        else: # 창 유지
            QCloseEvent.ignore()

app = QApplication(sys.argv) 
inst = qtApp() 
app.exec_() 
