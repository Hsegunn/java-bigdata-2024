# file: p25_usingModule.py
# desc: 모듈 사용

# import calc as c # calc.py 사용
from calc import mul # mul() 함수명만 사용하면 됨

from Math import Math # from Math는 모듈(파일이름) import Math는 클래스이름

from day03.p22_carClass import Car # 디렉토리(패키지).모듈명

if __name__== '__main__': ## java void main과 동일
    result = mul(10,7)
    print(result)

    print(__name__) #__main__ = 메인엔트리

    myMath = Math()
    print(myMath.solv(10))