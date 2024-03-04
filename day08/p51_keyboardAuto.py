# file: p51_keyboardAuto.py
# desc: 키보드 자동화 with PyAutoGui
import pyautogui as auto
import pyperclip as clip
'''
한글 입력은 
> pip install pyperclip
'''

# auto.mouseInfo()
# auto.click(485, 620)
auto.press('enter')
auto.write("print('Hello,Python!')", interval=0.01)
auto.write("\n", interval=0.01)
auto.typewrite("print('Life is short, You need python')", interval=0.01) # write()와 동일

# 키보드 프레스 기능
auto.press('enter'); auto.press('A')
# # 키보드 단축키로 입력
# auto.hotkey('ctrl', 'a') # 전체 선택
# auto.hotkey('ctrl', 'c') # 복사
# auto.press('esc'); auto.press('enter'); auto.press('enter'); auto.press('enter')
# auto.hotkey('ctrl', 'v') # 붙여넣기

# 한글은 pyautogui에서 입력할 수 없음
clip.copy('안녕하세요. 파이썬입니다') # 클립보드에 한글내용을 저장
auto.hotkey('ctrl','v') # 붙여넣기





