# file: p05_dict.py
# desc: 딕셔너리, 집합 자료형 학습

spiderMan = { 'name':'Peter Parker', 'age':18, 'weapon': 'Web shooter', 'friends':['ironMan','Thor','Captain America']}

## 출력
print(spiderMan)
print(spiderMan['name'])

## 값 추가
spiderMan['job'] = 'CameraMan'
print(spiderMan)

## 값 삭제
del spiderMan['friends']
print(spiderMan)

## 딕셔너리 함수
print(spiderMan.keys()) # 딕셔너리에 존재하는 키목록
print(list(spiderMan.keys())) # 키 목록을 리스트형태로 형변환
print(spiderMan.items()) # 딕셔너리 모든 아이템 출력
print(spiderMan.get('job')) # 딕셔너리의 값 가져오기

print('friends' in spiderMan) # 딕셔너리안에 키가 존재하는 여부 확인
print(spiderMan.values())

res = spiderMan.pop('job')
print(res)
print(spiderMan.pop('age'))
print(spiderMan)

## 데이터 삭제
spiderMan.clear()
print(spiderMan)

## 완전 삭제
del spiderMan 
print(spiderMan)

## 집합 : 중복허용X , 순서 X
# set([1,2,3,4,3,2,1]) = {1,2,3,4} 
