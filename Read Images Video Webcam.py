# Read Image

import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)


# Read Video

import cv2
frameWidth = 1280
frameHeight = 720
cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()


# Read WebCam

import cv2
frameWidth = 1280
frameHeight = 720
brightness = 150
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
