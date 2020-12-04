import cv2
import  numpy as np

##### IMG Cropped and Resize #####
img = cv2.imread("Resource/fotoApip.jpg")
print(img.shape) # console to size

# (width,height)
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image", img)
cv2.imshow("Image resize", imgResize)
cv2.imshow("Image crop", imgCropped)

cv2.waitKey(0)
