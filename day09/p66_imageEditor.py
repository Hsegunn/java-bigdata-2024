# file: p66_imageEditor.py
# desc: PyQt 이미지 에디터
'''
qrc 파일을 사용하려면
> pyrcc5 "resources.qrc" -o "resources_rc.py"
'''
'''
imutils 
> pip install imutils
'''

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
# 리소스 파일 추가
import resources_rc
# OpenCV 추가
import cv2, imutils

class WinApp(QMainWindow): # QWidget 아님
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()
    
    def initUI(self):
        # uic.loadUi('./day09/pyNewPaint.ui', self) # VSCode 실행용
        uic.loadUi('C:/Source/java-bigdata-2024/day09/pyNewPaint.ui', self) # PyInstaller용
        # self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.setWindowIcon(QIcon('C:/Source/java-bigdata-2024/day09/imgs/editor.png')) 

        self.setWindowTitle('이미지에디터 v0.5')
        ## 이미지 추가 / 여러가지 UI에 대한 초기화
        # pixmap = QPixmap('./day09/cat.jpg').scaledToHeight(471)
        pixmap = QPixmap('cat.jpg').scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.brushColor = Qt.red # 빨간색이 기본
        ## UI 초기화 끝
        self.show()

    def initSignal(self):
        # 메뉴/툴바 액션에 대한 시그널 처리함수 선언...
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Exit.triggered.connect(self.actionExitClicked)
        self.action_PenRed.triggered.connect(self.actionPenRedClicked)
        self.action_PenGreen.triggered.connect(self.actionPenGreenClicked)
        self.action_PenBlue.triggered.connect(self.actionPenBlueClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)
        # 변환 메뉴 추가
        self.action_Grayscale.triggered.connect(self.actionGrayscaleClicked)
    def actionBlurClicked(self):
        # tmpPath = './day09/temp.png'
        tmpPath = './temp.png'
        pixmap = self.lblCanvas.pixmap() # 라벨에 있는 그림을 pixmap 변수에 저장
        pixmap.save(tmpPath)
        image = cv2.imread(tmpPath)
        blur = cv2.blur(image, (10,10))
        blurImg = QImage(blur, blur.shape[1], blur.shape[0], blur.strides[0], QImage.Format_BGR888)
        self.lblCanvas.setPixmap(QPixmap.fromImage(blurImg))

    def actionGrayscaleClicked(self):
        # temp.png와 같은 형태로 임시 이미지저장
        # openCV로 불러와서 그레이스케일로 변경
        # 변경한 이미지를 다시 pixmap으로 변환한 뒤 lblCanvas에 올림
        # tmpPath = './day09/temp.png'
        tmpPath = 'temp.png'
        pixmap = self.lblCanvas.pixmap() # 라벨에 있는 그림을 pixmap 변수에 저장
        pixmap.save(tmpPath)
        image = cv2.imread(tmpPath)
        grayImg = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_Grayscale16)
        self.lblCanvas.setPixmap(QPixmap.fromImage(grayImg))
    
    def actionNewClicked(self):
        canvas = QPixmap(self.lblCanvas.width(), self.lblCanvas.height())
        canvas.fill(QColor('white'))
        self.lblCanvas.setPixmap(canvas)

    def actionOpenClicked(self):
        image = QFileDialog.getOpenFileName(self, '이미지 열기','','Image file(*.jpg;*.jpeg;*.png)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.lblCanvas.adjustSize()

    def actionSaveClicked(self):
        filePath, _=QFileDialog.getSaveFileName(self, '이미지 열기','','Image file(*.png)')
        if filePath == '': return
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(filePath)

    def actionExitClicked(self):
        cv2.destroyAllWindows()
        exit(0) # 종료

    def actionPenRedClicked(self):
        self.brushColor = Qt.red
    def actionPenGreenClicked(self):
        self.brushColor = Qt.green
    def actionPenBlueClicked(self):
        self.brushColor = Qt.blue

    def actionAboutClicked(self):
        QMessageBox.about(self,'알림','이미지 에디터 v0.5')

    def mouseMoveEvent(self, e) -> None:
        print(e.x(),e.y()-55)
        brush = QPainter(self.lblCanvas.pixmap()) # lblCanvas에 브러쉬 하나를 생성
        brush.setPen(QPen(self.brushColor, 3.5, style=Qt.SolidLine, cap=Qt.RoundCap))
        brush.drawPoint(e.x(),e.y()-55)
        brush.end()
        self.update() # 화면 업데이트

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes :
            cv2.destroyAllWindows()
            QCloseEvent.accept()
        else: 
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())
    
