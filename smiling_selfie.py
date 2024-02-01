import cv2
import mediapipe as mp
import pyautogui
import winsound

x1=0
y1=0
x2=0
y2=0
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
camera = cv2.VideoCapture(0)
while True:
    _ , image = camera.read()
    image = cv2.flip(image,1)
    fh, fw, _ = image.shape
    rgb_image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results=face_mesh.process(rgb_image)
    landmark_points = results.multi_face_landmarks
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id, landmark in enumerate(landmarks):
            x = int(landmark.x*fw)
            y = int(landmark.y*fh)
            if id==43:
                x1=x
                y1=y
            if id==287:
                x2=x
                y2=y
        dist = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
        print(dist)
        if dist > 90:
            cv2.imwrite("selfie.png", image)
            winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
            cv2.waitKey(100)
                # cv2.circle(image,(x,y),5,(0,255,0),cv2.FILLED)
                # if y>200:
                #     pyautogui.press('space')
                #     winsound.Beep(2500,100)
    cv2.imshow("Auto Selfie :)", image)
    key = cv2.waitKey(100) 
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()
