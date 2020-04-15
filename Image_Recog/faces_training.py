import os
import numpy as np
from PIL import Image
import cv2
import pickle

def trainusrs():
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))
    imgs_dir = os.path.join(CURR_DIR,"Images")

    face_cascade = cv2.CascadeClassifier(str(CURR_DIR + '/cascades/data/haarcascade_frontalface_default.xml'))
    pface_cascade = cv2.CascadeClassifier(str(CURR_DIR+'/cascades/data/haarcascade_profileface.xml'))


    face_ids={}

    curr_id = 0
    labels_to_faces=[]
    faces_to_train=[]
    counter=1
    #checking through all Saved faces
    for root,dirs,files in os.walk(imgs_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                img_label = os.path.basename(root).replace(" ","-").lower()
                img_path = os.path.join(root,file)
                
                if not img_label in face_ids:
                    face_ids[img_label]=curr_id
                    curr_id+=1
                curr_face_id = face_ids[img_label]
                
                #converting image to grayscale image
                grayscl_img = Image.open(img_path).convert("L") 
                #converting image to array of pixel values
                img_array = np.array(grayscl_img,"uint8")
                
                faces_found = face_cascade.detectMultiScale(img_array, scaleFactor=1.4, minNeighbors=5)
                pfaces_found = pface_cascade.detectMultiScale(img_array, scaleFactor=1.4, minNeighbors=5)
                
                for (x,y,w,h) in faces_found:
                    #append region of interest to train them
                    roi = img_array[y:y+h, x:x+w]
                    cv2.imwrite(str('img'+str(counter)+'.png'),roi)
                    counter+=1
                    faces_to_train.append(roi)
                    labels_to_faces.append(curr_face_id)
                    
                for (x,y,w,h) in pfaces_found:
                    #append region of interest to train them
                    roi = img_array[y:y+h, x:x+w]
                    cv2.imwrite(str('img'+str(counter)+'.png'),roi)
                    counter+=1
                    faces_to_train.append(roi)
                    labels_to_faces.append(curr_face_id)

    #save face_id with its label (dictionary) in a pickle file
    with open(str(CURR_DIR+"/face_labels.pickle"),"wb") as fw:
        pickle.dump(face_ids,fw)

    # print('len of face ids = {}'.format(len(faces_to_train)))
    # print('len of labels = {}'.format(len(labels_to_faces)))

    print('Training Faces...')
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces_to_train,np.array(labels_to_faces))
    face_recognizer.save(str(CURR_DIR + "/trained_faces.yml"))

    print('DONE')

# trainusrs()