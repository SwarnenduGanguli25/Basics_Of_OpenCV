import cv2
import numpy as np

# SHAPES & TEXT

img = np.zeros((512, 512, 3), np.uint8)   # As all zeroes, so BLACK background
# print(img)
# img[:]= 255,0,0
# B,G,R FORMAT   0,0,0 -> BLACK  255,255,255 -> WHITE
# [:] -> WHOLE IMAGE   [200:300,100:300] -> CROPPED PART

# (IMG, START COORDINATES, END COORDINATES, BGR, THICKNESS)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)  # LINE
cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)  # RECTANGLE
# cv2.rectangle(img,(0,0),(250,350),(0,0,255), cv2.FILLED)  RECTANGLE FILLED

# (IMG, CENTRE COORDINATES, RADIUS, BGR, THICKNESS)
cv2.circle(img,(400,50),30,(255,255,0),5)  # CIRCLE
# cv2.circle(img,(400,50),30,(255,255,0), cv2.FILLED)   CIRCLE FILLED

# (IMG, OUR TEXT, START COORDINATES, FONT, SCALE, BGR, THICKNESS)
cv2.putText(img," OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)   # TEXT ON IMAGE

cv2.imshow("Image",img)
cv2.waitKey(0)