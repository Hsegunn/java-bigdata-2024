#file: p12.gugudan.py
#desc: 구구단 프로그램

print('구구단 프로그램 ver99')
for x in range(2 , 10): # 2단~9단까지
    print(f'{x}단 시작 >>>>>')
    for y in range(1 , 10): # 1~9까지
      print(f'{x}X{y}={x * y:2d}', end='\t')
    print() # 아무런 내용없이 엔터만 출력  
