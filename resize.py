import cv2
import imutils

image=cv2.imread("ironman1.jpg")
resizeImg=imutils.resize(image,width=300)
cv2.imshow("Original image",image)
cv2.imshow("Resized imge",resizeImg)

