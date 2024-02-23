# file: p19_fileRead.py
# desc: 텍스트파일 읽기

f = open('./day03/CHANGELOG.md', mode='r', encoding='utf-8')

while True:
    read = f.readline() # 한줄 씩
    if not read: break #  더 이상 읽을 값이 없으면 반복분 탈출
    print(read.replace('\n',''))

f.close()