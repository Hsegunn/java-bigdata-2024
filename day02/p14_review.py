# file: p14_review.py
# desc: 되새김문제

#Q1
print('Q1')
a = 'Life is too short, you need python'
if 'wife' in a: 
    print('wife')
elif 'python' in a and 'you' not in a: 
    print('python')
elif 'shirt' not in a: 
    print('shirt')
elif 'need' in a: 
    print('need')
else: print('none')

#Q2
print('Q2')
result = 0
i = 1
while i <= 1000:
    if i % 3 ==0:
        result += i
    i += 1
print(result)

#Q3
print('Q3')
i = 0
while True:
    i += 1
    if i > 5:
        break
    print('*' * i)

#Q4
print('Q4')
for i in range(1,101):
    print(i,end=', ')
print()

#Q5
print('Q5')
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

#Q6
print('Q6')
number = [1,2,3,4,5]
res = [n * 2 for n in number if n % 2 ==1] 
print(res)