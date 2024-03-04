# 빅데이터 언어 2024
빅데이터 자바 개발자 파이썬 학습 리포지토리

## 1일차 
- 파이썬 개발환경
  - [깃헙](https://github.com/) 가입
  - [깃](https://git-scm.com/downloads) 설치
  - [깃헙 데스크탑](https://desktop.github.com/) 데스크탑 설치
  - [파이썬](https://www.python.org/) 설치
  - [Visual Studio Code](https://code.visualstudio.com/) 설치
  - [나눔고딕코딩 글자체](https://github.com/naver/nanumfont) 설치
- 파이썬 학습
  - 파이썬 개요
    - 1990년 네덜란드 개발자 귀도 반 로섬이 개발
    - 쉽고 간결한 문법, 무료, 빠른 개발속도
  - 파이썬 기초문법
    - 숫자형 (정수, 실수, 진수)
    ```python
    # 변수만 선언, 값만 할당하면 숫자형으로 지정
    # C, C++, C#, Java 처럼 형지정이 없음
    val = 10 # 정수형
    val = 2.15 # 실수형

    # 특수 숫자형
    binVal = 0b11111111 # 255 (컴퓨터 때문) (2진수)
    octVal = 0o11 # 9 1~7 10(8) ("") (8진수)
    hexVal = 0xFF # 255 0~9ABCDEF ("") (16진수)
    print('2진수',binVal, '8진수',octVal, '16진수', hexVal) 
    ```
    - 문자(특수형태 리스트)열 (연산, 문자열 포맷)
    ```python
    # '', "" 모두 사용 가능
    c = "Hello, 'Ashley'"
    print(c)
    ```
    - 리스트, 튜플 (연산, 함수)
      - 리스트는 수정, 삭제 가능
      - 튜플은 수정, 삭제 불가 그 외는 리스트와 동일

## 2일차
- 파이썬 학습
  - 파이썬 기초문법
    - 딕셔너리, 집합
    - 불형
    - None형
    - 제어문(if, while, for)
    - 제어문 연습
    - 함수

## 3일차
- 파이썬 학습
  - 파이썬 기초 문법
    - 입출력
    - 객체지향

## 4일차
- 파이썬 학습
  - 파이썬 기초문법
    - 모듈, 패키지
    - ★(중요)★ 예외처리, 디버깅 : 디버깅하면서 예외를 찾고 예외처리
    - 내장 함수
    - 표준 및 외부 라이브러리

## 5일차
- 파이썬 응용 
  - 파이썬 응용
    - OS 내 디렉토리 검색
    - 아스키 및 유니코드
    - 주소록 앱 만들기
    
    ```python
    class Contact: # 주소록 클래스
      def __init__(self, name, phoneNumber, eMail, addr) -> None: # 생성자
          self.__name = name
          self.__phoneNumber = phoneNumber
          self.__eMail = eMail 
          self.__addr = addr

      # 사용자가 원하는 형태로 출력
      def __str__(self) -> str: # 원래 출력 형태 <__main__.Contact object at 0x00000254ED7A2120>
          res = (f'이  름 : {self.__name}\n' 
                f'핸드폰 : {self.__phoneNumber}\n'
                f'이메일 : {self.__eMail}\n'
                f'주  소 : {self.__addr}')
          return res

       # 연락처 여부 확인
      def isNameExist(self, name):
          if self.__name == name: # 찾는 이름 존재
              return True
          else:
            return False
          
      def getInfo(self):
          return self.__name, self.__phoneNumber, self.__eMail, self.__addr
    ```

    ![주소록앱](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata01.gif)

    - windows App 만들기(PyQt 5)

    ![QtApp](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata02.png)
    
## 6일차 (24.02,28)
  - 파이썬 학습
    - PyQt5 학습 이어서
      - QWidget 자식 클래스 종류 학습
      
      ![QtApp](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata03.png)

      -  Naver 뉴스API로 검색 앱 만들기 

      ![NaverApp](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata04.png)

## 7일차
  - 파이썬 학습
    - PyQt5 이어서
      - Naver 뉴스 API 검색 앱 마무리
    - json 학습
    - PyQt5
      - 스레드 개념과 학습

      ![스레드](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata05.png)

      - TTS
      - QRcode 생성기

      ![QR](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata06.png)

      - 구글 번역기앱

      ![구글번역](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata07.png)

## 8일차
- 파이썬 학습
  - 파이썬 자동화
    - PyAutoGui 모듈 (마우스, 키보드, 화면캡쳐)
    - 슬랙 webhook으로 모바일 메세지 전송
      
    <!-- ![슬랙](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata08.png) -->
    <!-- html 태그로 이미지를 삽입하면 문제없음 -->
    <img src = "https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata08.png" width="300">
    
    - Tesseract 프로그램으로 이미지에서 글자 추출 (인식율울 높이려면 직접 트레이닝 데이터를 생성해야 함)

    ![구글번역](https://raw.githubusercontent.com/Hsegunn/java-bigdata-2024/main/images/bigdata09.png)

## 9일차
- 파이썬 학습
  - 이미지 처리 OpenCV
  - 플라스크 웹서버
  - 그림에디터 만들기
  - Jupyter Notebook 사용법 (빅데이터 분석, 코딩 테스트)




