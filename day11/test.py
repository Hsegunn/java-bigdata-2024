# 4. while 문을 사용, 1부터 1000 까지 에서 3과 5의 배수를 모두 구한뒤,
# result.txt에 저장하는 프로그램을 작성하세요.

res = 1
f = open('./day11/result.txt', mode='w', encoding='utf-8') # './폴더위치/result.txt'
while res <= 1000:
    if res % 3 ==0:     
        print(f'3의배수:{res}', end=' ')
        f.write(f'3의배수:{res}\n')
    elif res % 5 ==0:
        print(f'5의배수:{res}', end=' ')
        f.write(f'5의배수:{res}\n')
    res += 1
f.close