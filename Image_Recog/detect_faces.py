import numpy as np 
import cv2
import pickle
import time
import os

capture = cv2.VideoCapture(0)
curr_dir = os.path.dirname(os.path.abspath(__file__))
face_cascade = cv2.CascadeClassifier(str(curr_dir+'/cascades/data/haarcascade_frontalface_default.xml'))
psc = cv2.CascadeClassifier(str(curr_dir+'/cascades/data/haarcascade_profileface.xml'))
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(str(curr_dir+"/trained_faces.yml"))

PERSON_CONF = {}
tot_faces=0

faceid_to_name = {}
def setup():
    global faceid_to_name
    with open(str(curr_dir+"/face_labels.pickle"),"rb") as fr:
        name_to_faceid = pickle.load(fr)
        faceid_to_name = {v:u for u,v in name_to_faceid.items()}
def detect():
    global faceid_to_name
    global tot_faces
    global PERSON_CONF
    start_time = time.time()
    while True:
        if(time.time()-start_time>=5):
            capture.release()
            break
        ret, frame = capture.read()
        frame=cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_found = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)
        pface = psc.detectMultiScale(gray,scaleFactor=1.4,minNeighbors=5)

        for (x,y,w,h) in pface:
            print(x,y,w,h)
            #roi=region of interest
            roi_gray = gray[y:y+h, x:x+w]
            # img_detected = "my-img.png"
            # cv2.imwrite(img_detected, roi_gray)

            face_id,confidence = face_recognizer.predict(roi_gray)
            print(faceid_to_name[face_id])

            color=(0,255,255)
            stroke=1
            cv2.rectangle(frame,(x,y),(x+w,y+h), color,stroke)
            if confidence>50:
                tot_faces+=1
                if face_id not in PERSON_CONF:
                    PERSON_CONF[face_id]=confidence
                else:
                    PERSON_CONF[face_id]+=confidence
                cv2.putText(frame,faceid_to_name[face_id],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(125,125,0),2,cv2.LINE_AA)
                cv2.putText(frame,str(round(confidence,2)),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,1,(125,125,0),2,cv2.LINE_AA)


        for (x,y,w,h) in faces_found:
            print(x,y,w,h)
            #roi=region of interest
            roi_gray = gray[y:y+h, x:x+w]
            # img_detected = "my-img.png"
            # cv2.imwrite(img_detected, roi_gray)

            face_id,confidence = face_recognizer.predict(roi_gray)
            print(faceid_to_name[face_id])

            color=(0,0,255)
            stroke=2
            cv2.rectangle(frame,(x,y),(x+w,y+h), color,stroke)
            if confidence>50:
                tot_faces+=1
                if face_id not in PERSON_CONF:
                    PERSON_CONF[face_id]=confidence
                else:
                    PERSON_CONF[face_id]+=confidence
                cv2.putText(frame,faceid_to_name[face_id],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(125,125,0),2,cv2.LINE_AA)
                cv2.putText(frame,str(round(confidence,2)),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,1,(125,125,0),2,cv2.LINE_AA)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            capture.release()
            break

    capture.release()
    cv2.destroyAllWindows()
def authenticate(person):
    setup()
    detect()
    high_conf=-1
    high_id=-1
    if tot_faces==0:
        return False
    for x in PERSON_CONF:
        if PERSON_CONF[x]>high_conf:
            high_conf=PERSON_CONF[x]
            high_id=x
    high_conf/=tot_faces
    if high_conf>50 and person.lower()==faceid_to_name[high_id].lower():
        return True
    else:
        return False

    
# setup()
# detect()