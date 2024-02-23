# file: p23_carSample.py
# desc: Car 클래스 사용

from p22_carClass import Car

myCar = Car('12가3456') # 클래스를 사용, 객체를 하나생성(instance)
yourCar = Car('87호 8733')

# print(myCar)
# print(yourCar)
# myCar.__carNum = '12가3456'  더 이상 사용불가
myCar.company = '현대'
myCar.fuelType = '가솔린'
myCar.carType = '하이브리드'
myCar.color = '흰색'
myCar.releaseYear = '2018'
# yourCar.carNum = '87호 8733'
print(myCar)


myCar.getCarColor()
myCar.start()
myCar.accel()
yourCar.start()
myCar.turnRight()
myCar.turnLeft()
myCar.brake()

