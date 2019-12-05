import serial
import cv2
import numpy as np

from os import listdir
from os.path import isfile, join
from socket import *
class SocketInfo():
    HOST=""
    PORT=8888
    BUFSIZE=1
    ADDR=(HOST,PORT)
class socketInfo(SocketInfo):
    HOST="127.0.0.1"
    
csock = socket(AF_INET,SOCK_STREAM)
csock.connect(socketInfo.ADDR)
print("connect is success")

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
)
data_path = 'faces/'
data_path2 = 'faces2/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]
onlyfiles2 = [f for f in listdir(data_path2) if isfile(join(data_path2,f))]
Training_Data, Labels = [], []
Training_Data2, Labels2 = [], []
print("Loading...")
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
for i, files in enumerate(onlyfiles2):
    image_path2 = data_path2 + onlyfiles2[i]
    images2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)
    Training_Data2.append(np.asarray(images2, dtype=np.uint8))
    Labels2.append(i)
Labels = np.asarray(Labels, dtype=np.int32)
Labels2 = np.asarray(Labels2, dtype=np.int32)
model = cv2.face.createLBPHFaceRecognizer()
model2 = cv2.face.createLBPHFaceRecognizer()
model.train(np.asarray(Training_Data), np.asarray(Labels))
model2.train(np.asarray(Training_Data2), np.asarray(Labels2))
print("Model Training Complete!!!!!")
while True:
    if ser.readable():
        #res = ser.readline()
        #print(res.decode()[:len(res)-2])
        #move = res.decode()[:len(res)-2]
        commend = csock.recv(socketInfo.BUFSIZE, MSG_WAITALL)
        data = commend.decode("UTF-8")
        move = data
        print("move : " + move);
        if move=='1':
            print("Motion is detected!")
            #### 여기까지 Part2.py와 동일
            #### 여긴 Part1.py와 거의 동일 
            face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            def face_detector(img, size = 0.5):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)
                if faces is():
                    return img,[]
                for(x,y,w,h) in faces:
                    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
                    roi = img[y:y+h, x:x+w]
                    roi = cv2.resize(roi, (200,200))
                return img,roi   #검출된 좌표에 사각 박스 그리고(img), 검출된 부위를 잘라(roi) 전달
            #### 여기까지 Part1.py와 거의 동일 
            #카메라 열기 
            cap = cv2.VideoCapture(0)
            i=0
            while True:
                #카메라로 부터 사진 한장 읽기
                ret, frame = cap.read()
                # 얼굴 검출 시도 
                image, face = face_detector(frame)
                try:
                    #검출된 사진을 흑백으로 변환 
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    #위에서 학습한 모델로 예측시도
                    result = model.predict(face)
                    result2 = model2.predict(face)
                    #result[1]은 신뢰도이고 0에 가까울수록 자신과 같다는 뜻이다. 
                    if result[1] < 500:
                        #????? 어쨋든 0~100표시하려고 한듯 
                        confidence = int(100*(1-(result[1])/300))
                        # 유사도 화면에 표시 
                        display_string = str(confidence)+'% Confidence it is Chaejun'
                    #cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
                    if result2[1] < 500:
                        #????? 어쨋든 0~100표시하려고 한듯
                        confidence2 = int(100*(1-(result2[1])/300))
                        # 유사도 화면에 표시
                        display_string2 = str(confidence2)+'% Confidence it is Yejin'
                    #80 보다 크면 동일 인물로 간주해 UnLocked!
                    if confidence > 80:
                        cv2.putText(image, "Chaejun", (200, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow('Face Cropper', image)
                        cv2.putText(image,display_string2,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
                    else:
                       #75 이하면 타인.. Locked!!! 
                        #cv2.putText(image, "Not Chaejun", (200, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                        cv2.imshow('Face Cropper', image)
                        cv2.putText(image,display_string2,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
                    if confidence2 > 80:
                        cv2.putText(image, "Yejin", (200, 330), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow('Face Cropper', image)
                        cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
                    else:
                        #75 이하면 타인.. Locked!!!
                        #cv2.putText(image, "Not Yejin", (200, 330), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                        cv2.imshow('Face Cropper', image)
                        cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
                except:
                    #얼굴 검출 안됨 
                    cv2.putText(image, "Face Not Found", (200, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                    cv2.imshow('Face Cropper', image)
                    pass
                cv2.waitKey(1)
                i = i+1
                if i > 150:
                    commend = csock.recv(socketInfo.BUFSIZE, MSG_WAITALL)
                    data=commend.decode("UTF-8")
                    move = data
                    #res = ser.readline()
                    #move = res.decode()[:len(res)-2]
                    print("move : "+move)
                    if move != '1':
                        break
                    else:
                        cv2.putText(image, "detected", (200, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                        cv2.imshow('Face Cropper', image)
            cap.release()
            cv2.destroyAllWindows()
