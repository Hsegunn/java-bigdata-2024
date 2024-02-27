# file: p31_externalLib.py
# desc: 외부 라이브러리 사용법

# > pip install LibName
# Successfully installed / Requirement already satisfied가 나와야 함
# > pip unstall LibName
# Successfully unstalled가 나와야 함

from faker import Faker

fake = Faker('ko-KR') # 한국어 설정
print(fake.name())
print(fake.address())
# print(fake.profile())

dummyData = [(fake.profile()) for _ in range(10)]
print(dummyData)

## urllib3 외부 웹페이지 분석모듈
import requests
from bs4 import BeautifulSoup


# res = requests.get('http://www.naver.com')
# print(res.status_code)
# print(res.content) # 내용 가져오기

res = requests.get('http://www.naver.com')

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    