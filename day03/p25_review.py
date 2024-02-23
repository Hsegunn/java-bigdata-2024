# file: p25_review.py
# desc: 문제

# Q1
print('Q1')
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
print(is_odd(3))
print()

# Q2
print('Q2')
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)
print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))
print()

# Q3
# print('Q3')
# input1 = input('첫 번째 숫자를 입력하세요')
# input2 = input('두 번째 숫자를 입력하세요')
# input1 = int(input1)
# input2 = int(input2)
# total = input1 + input2
# print('두수의 합:',total)
# print()

# Q4
print('Q4')
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python") # 출력값이 다름 ( , 로 문자열 띄어쓰기)
print("".join(["you","need","python"])) # join 입력값이 없으므로 리스트 그대로 출력
print()

#Q5
print('Q5')
f1 = open('./day03/test2.txt', mode='w')
f1.write('Life is too short')
f1.close()

f2 = open('./day03/test2.txt', mode='r')
print(f2.read())
f2.close()
print()

#Q6
print('Q6')
user_input = input('저장할 내용을 입력')
f = open('./day03/test3.txt', mode='a')
f.write(user_input)
f.write('\n')
f.close





