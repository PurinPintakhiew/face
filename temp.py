import cv2
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#detector2 = cv2.CascadeClassifier("")

cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    img = frame.copy()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        face = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow("screen",img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
