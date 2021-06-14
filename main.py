import cv2
from time import sleep
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600) # define serial port for arduino

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0) # read from web camera

while True:
    success, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        value = int((x + (w/2))/3.4)
        valueStr = str(180 - value)
        print(value)
        ser.write(valueStr.encode())
        sleep(0.08) # minimal possible delay for arduino
        
    cv2.imshow('rez', img) # show output image for debug
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
