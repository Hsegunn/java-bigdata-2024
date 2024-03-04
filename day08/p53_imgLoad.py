# file: p53_imgLoad.py
# desc: PyAutoGul에서 이미지 읽어오기
import pyautogui as auto

# capImg = auto.locateOnScreen('./day08/screen.png') # 이미지 로드
# print(capImg)
# auto.click(capImg)

auto.alert('테스트', title='PuAutoGui')
auto.confirm('계속 진행하시겠습니까?')
text = auto.prompt('메세지 입력')
print(text)

pwd = auto.password('암호입력')
print(pwd)