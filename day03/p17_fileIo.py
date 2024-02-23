# file: p17_fileIo.py
# desc: 파일 입출력 학습

# 컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open(), close() / 파이썬은 안 닫아도 크게 지장없음
# 2. 통신 open(), close()
# 3. DB open(or connect), close()

# 언어체계 추가 ASCII(한글 cp949), 유니코드(UTF-8)
# 상대경로, 절대경로
# w는 매번 새로 파일생성, a는 기존파일에서 내용추가
# 로그 등을 남길 때는 a로 작업
f = open('./day03/sample.txt', mode='a', encoding='utf-8')
# 파일 쓰기 진행
f.write('안녕하세요. 파이썬\n') # 한 줄 내리기 '\n'
f.write('모두 화이팅\n')

f.close # 파이썬에서만 옵션. 다른언어에서는 close()
