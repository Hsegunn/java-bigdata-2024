# file: p52_screenCap.py
# desc: pyautogui로 화면 캡쳐하기
'''
> pip install pillow
'''
import pyautogui as auto
import time

startX, endX = 0, 1919
startY, endY= 0, 1079

auto.screenshot('./day08/screen.png',region=(startX, startY, endX-startX, endY-startY))

