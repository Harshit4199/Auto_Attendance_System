import cv2
import numpy as np
import  pandas as pd
import sqlite3

def attendence():

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainner/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    cam = cv2.VideoCapture(1)
    #   font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    present_list = []
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            if(conf>50):
                present_list.append(Id)

                if(Id==1):
                    Id="harshit"
                elif(Id==2):
                    Id="Edil"
                elif(Id==3):
                    Id="Kashish"
            else:
                Id="Unknown"
        #cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        #print(cv2.fromarray(im,str(Id),(x,y+h), font, 255))
            cv2.putText(im,str(Id),(x,y-10),font,0.55,(255,255,0),1)

        cv2.imshow('Detecting student',im)
        k = cv2.waitKey(10) & 0xFF
        if k == 27:
            break
    cam.release()
    cv2.destroyAllWindows()
    present_list = (list(dict.fromkeys(present_list)))
    print present_list
    return present_list

