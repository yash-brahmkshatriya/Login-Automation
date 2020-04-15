import numpy as np 
import cv2
import os
import time

curr_dir = os.path.dirname(os.path.abspath(__file__))
# img_dir = 'C:/Users/Dilip/Yash Codes/Python/Login_Automation/Image_Recog/Images'
img_dir = os.path.join(curr_dir,'Images')
print(img_dir)
# face_cascade = cv2.CascadeClassifier('C:/Users/Dilip/Yash Codes/Python/Login_Automation/Image_Recog/cascades/data/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(str(curr_dir + '/cascades/data/haarcascade_frontalface_default.xml'))
SCAN_SUCCESS = False

def setup(usrname):
    global img_dir
    img_dir = os.path.join(img_dir, usrname)
    os.mkdir(img_dir)

def capture_photos():
    global SCAN_SUCCESS
    cntr=1
    capture = cv2.VideoCapture(0)
    start_time = time.time()
    while True:
        if time.time()-start_time>4:
            capture.release()
            break
        found = False
        ret, frame = capture.read()
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_found = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)

        for (x,y,w,h) in faces_found:
            if found:
                break
            found = True
        if found:
            cv2.imwrite(str(img_dir+'/img'+str(cntr)+'.png'),frame)
            cntr+=1
        for (x,y,w,h) in faces_found:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),1)
        if found:
            SCAN_SUCCESS = True
        cv2.imshow('Frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            capture.release()
            break
    cv2.destroyWindow('Frame')
    return SCAN_SUCCESS
# setup('YEAHHHH')
# capture_photos()