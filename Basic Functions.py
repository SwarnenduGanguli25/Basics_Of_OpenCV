import cv2
import numpy as np

# BASIC FUNCTIONS

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # GRAYSCALE
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)    # BLUR
imgCanny = cv2.Canny(img, 150, 200)     # CANNY EDGES
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)   # DILATION
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)   # EROSION

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)