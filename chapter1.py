import cv2
import  numpy as np

# ##### IMAGE VIEW #####
# # open image
# img = cv2.imread("Resource/lena.png")
#
# # print result
# cv2.imshow("Output", img)
# cv2.waitKey(0)

##### Video VIEW #####
# open video from webcam
cap = cv2.VideoCapture(0)
cap.set(3,640) # set color
cap.set(4,480) # set ratio
cap.set(10,100) # set brigness

# showing video and quit with keypress
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
