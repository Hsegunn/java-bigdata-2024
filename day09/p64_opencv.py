# file: p64_opencv.py
# desc: OpenCV 계속

import cv2

samplePath = './day09/news.mp4'
faceCascade = cv2.CascadeClassifier('./day09/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) # 0은 웹캠 또는 문자열로 동영상 경로

while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue

    ## 영상 편집
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20,20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),color=(255,0,0), thickness=2) # color = (B,G,R)

    cv2.imshow('original',frame)
    cv2.imshow('gray',gray)


    key = cv2.waitKey(50) # 50ms 딜레이
    if key == ord('q'): # esc(27), q=ord('q')
        break

cap.release()
cv2.destroyAllWindows()