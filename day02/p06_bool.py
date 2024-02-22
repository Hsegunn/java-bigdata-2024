# file: p06_bool.py
# desc: 불타입, None타입 학습

# 참/거짓
a = True # 참
b = False # 거짓
print(a)
print(type(a)) # <class 'bool'>
print(type(1)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type('hi')) # <class 'str'>
print(type([1,2,3])) # <class 'list'>
print(type((1,2,3))) # <class 'tuple'>

print(a == b)
print(a == (not b))

# 참/거짓 구분은 빈값, 0, None False 그 외는 True
print(bool('H'))

# None 타입
None

c = None
a = 1
b = 0
print(c)
print(a+b) # a true(1) b false(0)





