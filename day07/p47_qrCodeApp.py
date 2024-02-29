# file: p47_qrCodeApp.py
# desc: PyQt5 QR코드 앱
# pip install qrcode

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import qrcode

class qtApp(QWidget): 
    def __init__(self) -> None: 
        super().__init__()  
        self.initUI()

    def initUI(self): # ui파일을 로드해서 화면디자인 사용
        uic.loadUi('./day07/qrApp.ui', self)
        self.setWindowTitle('QR 앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnGenerate.clicked.connect(self.btnGenerateClicked) # ui 파일 내 위젯은 자동완성 X

        self.show()

    def btnGenerateClicked(self):
        data = self.txtQrData.text()

        if len(data.strip()) == 0:
            QMessageBox.about(self, '경고','데이터를 입력하시오')
            return
        else:
            imgPath = './day07/qr.png'
            qrImage = qrcode.make(data)
            qrImage.save(imgPath)
            img = QPixmap(imgPath)
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))


    
    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:
            QCloseEvent.accept() 
        else: # 창 유지
            QCloseEvent.ignore()

app = QApplication(sys.argv) 
inst = qtApp() 
app.exec_() 
