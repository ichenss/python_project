import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("error")
while 1:
    ret, frame = cap.read()
    if not ret:
        print("read error")
        break
    frame_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    face = cv.CascadeClassifier("Face_ai/haarcascade_frontalface_alt2.xml")
    faces = face.detectMultiScale(frame_gray, scaleFactor=1.3)
    for x, y, w, h in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), color=(0,0,255), thickness=2)
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
