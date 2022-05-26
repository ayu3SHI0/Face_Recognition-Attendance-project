import cv2
import numpy as np
import face_recognition

imgModi = face_recognition.load_image_file('imagesBasic/modi.jpg')
imgModi = cv2.cvtColor(imgModi,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('imagesBasic/testt.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

facLoc = face_recognition.face_locations(imgModi)[0]
encodeModi = face_recognition.face_encodings(imgModi)[0]
cv2.rectangle(imgModi,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

facLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(facLocTest[3],facLocTest[0]),(facLocTest[1],facLocTest[2]),(255,0,255),2)

faceDis = face_recognition.face_distance([encodeModi],encodeTest)
result = face_recognition.compare_faces([encodeModi],encodeTest)
print(result,faceDis)
cv2.putText(imgTest,f'{result} {round(faceDis[0]),2}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('modi',imgModi)
cv2.imshow('test',imgTest)
cv2.waitKey(0)