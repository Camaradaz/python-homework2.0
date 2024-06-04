import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades 
                + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

cv2.namedWindow('Face Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Face Detection', 1920, 1080)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
					                      scaleFactor=1.3,
                                          minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x, y), (x+w, y+h),
        (0, 255, 0),4)

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()