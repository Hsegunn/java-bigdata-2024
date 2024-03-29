# file: p59_opencv.py
# desc: OpenCV 활용

# OpenCV 실시간 이미지 프로세싱 라이브러리
'''
> pip install opencv-python
'''
import cv2 

#print(cv2.__version__) # 설치 확인용

image = cv2.imread('./day09/cat.jpg', cv2.IMREAD_UNCHANGED) # cv.2 IMREAD_GRAYSCALE > 칼라이미지를 흑백으로 전환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width, channel = image.shape
print(width,height,channel)

sizeSmall = cv2.resize(image, (width//2, height//2)) 

# img_cropped = image[:(height//2),:(width//2)] # y축, x축
img_cropped = image[:,:(width//2)] # x축을 반으로 잘라 반만 나오도록


cv2.imshow('cat, color', image) # 원본
cv2.imshow('Reduced cat', sizeSmall) # 반으로 줄인 사이즈
cv2.imshow('cat, gray', gray) # 흑백
cv2.imshow('Half cat', img_cropped) # 흑백


cv2.waitKey(0)
cv2.destroyAllWindows()








