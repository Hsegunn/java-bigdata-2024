# file: p74_simpleNotepad.py
# desc: 간단한 메모장 만들기

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WinApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('./day10/simpleNotepad.ui', self)
        self.setWindowIcon(QIcon('./day10/editor.png'))
        self.setWindowTitle('Simple Note')
        self.file_path = None
        ## UI 초기화 끝
        self.show()

    def initSignal(self):
        # 메뉴/툴바 액션에 대한 시그널 처리함수 선언...
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Save_As.triggered.connect(self.actionSaveAsClicked)
        self.action_Quit.triggered.connect(self.actionQuitClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)

    def actionOpenClicked(self):
        global path

        path = QFileDialog.getOpenFileName(self, 'Open', '', 'text file(*.txt;*.text;*.log)')[0]
        self.title = 'test'
        if path:
            self.pteContent.setPlainText(open(path, mode='r', encoding='utf-8').read())
            self.title = path
            self.file_path = path


    def actionSaveClicked(self):
        try:
            if self.file_path is None:
                print('1')
                self.actionSaveAsClicked()
                print('2')
            else:
                with open(self.file_path, mode='w', encoding='utf-8') as f:
                    f.write(self.pteContent.toPlainText())
                self.pteContent.document().setModified(False)
                print('Saved')
        except:
            pass

    def actionSaveAsClicked(self):
        path = QFileDialog.getSaveFileName(self, 'Sava As', '', 'text file(*.txt;*.text;*.log)')[0]
        if path:
            self.file_path = path            
            self.actionSaveClicked() 
                                                  
    def actionQuitClicked(self):
        exit(0) # 종료

    def actionAboutClicked(self):
        QMessageBox.about(self, '심플노트패드', '심플 노트패드 v0.1')

    def closeEvent(self, QCloseEvent) -> None:
            re = QMessageBox.question(self, '종료','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No)
            if re == QMessageBox.Yes :
                QCloseEvent.accept()
            else: 
                QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())
    