
import cv2
face_cap =cv2.CascadeClassifier("C:/Users/User46/AppData/Roaming/Python/Python310/site-packages/cv2/data/ haarcascade_frontalface_default")

video_cap = cv2.VideoCapture(0)
while True:
    ret,data_video = video_cap.read()
    col = cv2.cvtColor(data_video,cv2.COLOR_BGR2GRAY)

    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize =(30,30),
        flags = cv2.CASCADE_SCALE_IMAGE

    )
    for (x, y, w, h) in faces:
        cv2.rectangle(data_video, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("face_live",data_video)
    if cv2.waitKey(10)== ord("a"):
        break
video_cap.release()
