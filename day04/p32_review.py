# file: p32_review.py
# desc: 문제풀이

# Q1
print('Q1')
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# Q2
print('Q2')
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
class MaxLimitCal(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
cal = MaxLimitCal()
cal.add(50)
cal.add(500)
print(cal.value)

# Q6
print('Q6')
list(map(lambda a: a*3, [1, 2, 3, 4]))

# Q7
print('Q7')
a = [-8, 2, 7, 5, -3, 5, 0, 1]
min(a)+max(a)
# Q11
print('Q11')
import datetime
curr = datetime.datetime.now() 
print(curr)