# file: p54_capWeather.py
# desc: 네이버 날씨 화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

regions = ['서울', '강원', '대전', '대구', '부산']
# auto.mouseInfo()
for regions in regions:
    auto.moveTo(80,110,duration=0.5)
    auto.leftClick()
    for _ in range(10):
        auto.press('delete')
    time.sleep(0.5)

    clip.copy(f'{regions} 날씨')
    auto.hotkey('ctrl','v') # 붙여넣기
    time.sleep(0.5)

    auto.press('enter')
    time.sleep(1.0)

    startX, startY = 33, 231
    endX, endY = 704, 879
    auto.screenshot(f'./day08/{regions}날씨.png', region=(startX, startY, endX-startX, endY-startY))
    # auto.screenshot()만 사용하면 macos에서 동작안함
    # im = auto.screenshot(region=(startX, startY, endX-startX, endY-startY))
    # im.save(f'./day08/{regions}날씨.png')
print('저장완료')

