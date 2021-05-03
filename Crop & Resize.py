import cv2

# OPENCV -> (WIDTH, HEIGHT) CONVENTION
# DIRECT IMAGE -> (HEIGHT, WIDTH) CONVENTION

# CROP AND RESIZE

img = cv2.imread("Resources/lambo.png")
print(img.shape)   # ORIGINAL IMAGE DIMENSIONS

imgResize = cv2.resize(img, (300, 200))   # RESIZE (WIDTH, HEIGHT)
print(imgResize.shape)   # RESIZED IMAGE DIMENSIONS

imgCropped = img[0:200, 200:500]    # CROPPING (HEIGHT, WIDTH)

cv2.imshow("Image", img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)