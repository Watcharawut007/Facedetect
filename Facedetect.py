import cv2
import RPi.GPIO as GPIO
cap =cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ledpin = 3
listled=[]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin,GPIO.OUT)

while True :
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.1,4)
    if len(faces)>0:
        for (x,y,w,h) in faces :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            print('1')
            if len(listled)>9:
                listled.pop(0)
                listled.append(1)
            else:
                listled.append(1)
            if (listled.count(1)>4):
                GPIO.output(ledpin,GPIO.HIGH)
    else:
        print("0")
        if len(listled)>9:
                listled.pop(0)
                listled.append(0)
        else:
            listled.append(0)
        if (listled.count(0)>8):
            GPIO.output(ledpin,GPIO.LOW)

    cv2.imshow('frame',frame)
    cv2.waitKey(1)