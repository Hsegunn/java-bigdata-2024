# file: p55_katalkAuto.py
# desc: 카톡 PC에서 자동으로 메세지 보내기
# pyautogui.ImageNotFoundException 예외 자주 발생
import pyautogui as auto
import pyperclip as clip
import time
import os

katalkLoc = auto.locateOnScreen('./day08/findLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.doubleClick(clickPos)
time.sleep(0.5)

groupLoc = auto.locateOnScreen('./day08/findLoc2.png')
clickPos = auto.center(groupLoc)
auto.doubleClick(clickPos)
time.sleep(0.5)

clip.copy('자동으로 보내는 메시지. 자주 하지마세요~')
auto.hotkey('ctrl','v')
auto.press('\n')