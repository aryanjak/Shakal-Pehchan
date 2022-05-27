import cv2
face_cascad = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
img = cv2.imread("group-people-multi-ethnic-isolated-32199406.jpg")
#cv2.waitKey(1000)
faces = face_cascad.detectMultiScale(img,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img , (x,y) , (x+w,y+h) , (255,0,0) , 5)

cv2.imshow("img123" , img)
cv2.waitKey()   