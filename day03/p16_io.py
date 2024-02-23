# file: p16_io.py
# desc: 입출력 학습

# input() 함수 기본
# res = input('인사말 입력 >')
# print(res)

# input()로 받는 값은 모두 문자열
# num = input('곱할 수를 입력>')
# print(type(num)) 
# num = int(num) # 숫자를 입력해서 계산을 할 때는 형변환이 필요
# print(num * 2)

# num = int (input('2로 곱할 숫자 입력 > '))
# print(num * 2)

## 여러값 입력
# int(40.2) #40
# int('50') #50 
# int('40.2') # X
# int((10,20,30)) # X 튜플은 바로 int 변환할 수 없다

# 튜플의 괄호중 할당을 받는 쪽의 괄호는 생략 가능
# (a1, a2, a3) = input('합산 3개의 값을 입력(구분자는 space) >').split(' ')
(a1, a2, a3) = map(int, input('합산 3개의 값을 입력(구분자는 space) >').split(' '))

print(a1)
print(a2)
print(a3)
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
sum = a1 + a2 + a3
print(f'합계는 {sum}')

