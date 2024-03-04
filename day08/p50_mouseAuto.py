# file: p50_mouseAuto.py
# desc: PyAutoGui로 마우스 조작

'''
파이썬 모듈 설치 시 명령 프롬프트보다 VsCode내 터미널에서 설치를 추천
PyAutoGui 모듈 설치
> pip install pyautogui
'''

import pyautogui as auto

print(auto.size()) # 모니터 해상도
print(auto.position()) # 현재커서 좌표

# pyAutoGui 마우스 설정 창
# pillow 모듈이 같이 설치되어야 색상 표시가능 (pip install pillow)
#auto.mouseInfo()

## 절대좌표 마우스 이동 
auto.moveTo(100,51) # (0.0)은 이동이 안됨
auto.moveTo(678,51,duration=1.5)  #X축 678, Y축 51으로 1.5초 동안 이동
auto.moveTo(1210,568,duration=1.5) 

## 상대좌표 마우스 이동
#auto.move(505,505,duration=1.5) # 현재 위치에서 X축 500, Y축 500으로 1.5초 동안 이동

## 마우스 클릭
# auto.leftClick(678,51) # 해당 위치 클릭
# auto.rightClick(790,300) # 해당 위치 클릭
auto.click(clicks=4, interval=0.1, button='left') # 왼쪽버튼을 소스코드 에디터에서 네번 선택하면 모든 글을 전체선택

## 마우스 드래그
auto.leftClick(1422, 168, duration=1.0) # 1422,168 에서 왼쪽 마우스 클릭 후 1초 대기했다가
auto.dragTo(983,550,duration=2.0,button='left')
# auto.dragRel(983,550,duration=2.0,button='left') # 현재위치에서 500,400으로 1초동안 드래그

## 마우스 휠
auto.scroll(200) # 양수는 위로
auto.scroll(-100) # 음수는 아래로 스크롤



