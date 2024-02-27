# file: p27_exceptionHandle.py
# desc: 예외처리2

# while True:
#     try:
#         select = input('메뉴입력 1. 저장, 2. 검색, 3. 종료 >>')
#     except:
#         print('예외발생. 입력을 정확히 해주십시오')
#         continue
#     if select == '1':
#         print('입력')
#     elif select == '2':
#         print('검색')
#     elif select == '3':
#         break
#     else:
#         continue

class Chicken:
    def fly(self):
        raise NotImplementedError
koko = Chicken()
try:
    koko.fly()
except Exception as e:
    print('닭은 못날아요', e.args) # NotImplementedError는 추가 예외메세지가 없음

