# file: p08_review.py
# desc: 되새김 문제

# Q2
print('Q2')
a = 13
print('a는 ', end = '')
res = a % 2
if a % 2 == 0:
    print('짝수')
else:
    print('홀수')
# Q3
print('Q3')
pin = '881120-1068234'
yyyymmdd = pin[0:5+1]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q5
print('Q5')
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

# Q6
print('Q6')
a = [1,3,5,4,2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# Q10
print('Q10')
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)