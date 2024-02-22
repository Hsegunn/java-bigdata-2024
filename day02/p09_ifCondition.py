# file: p09_ifCondition.py
# desc: if 제어문

money = 5000

if money >= 5000:
    # indentation () tab == space 4
    print('택시타고 가')
    print('부럽네')
elif money < 500 and money >= 2500:
    print('홈플러스')
    print('집까지 걸어감')
else:
    print('걸어가')
    print('돈도 없는게.')