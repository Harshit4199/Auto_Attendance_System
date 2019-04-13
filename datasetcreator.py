import cv2
import numpy as np

def create_data(name,Id):
    cam = cv2.VideoCapture(1)
    detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    print(detector)

    sampleNum=1
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))
        cv2.imshow("ADDING... "+name,img)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            #incrementing sample number
            sampleNum=sampleNum+1
            #saving the captured face in the dataset folder
            cv2.imwrite("dataset/User."+str(Id) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])



        #wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 20
        elif sampleNum>100:
            break
    cam.release()
    cv2.destroyAllWindows()
