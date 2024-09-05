import cv2 as cv
import numpy as np

img = cv.imread('images/cats.jpg')
cv.imshow("image",img)

#averaging method for blur image
blur = cv.blur(img,(3,3))
cv. imshow("blur",blur)

# gaussian blur --> natural and less bluring the image
#(3,3) shows kernel size large kernel size --> blur increase
gauss = cv.GaussianBlur(img,(3,3),0) #0 -->  specifies the standard deviation of the Gaussian kernel along the X-axis  A larger sigmaX value results in a smoother blur. If sigmaY is not specified, it is taken as equal to sigmaX
cv.imshow("gauss",gauss)

#median --> to be more effective in reducing moise in an image as compared to averaging and gaussian and preety good to remove salt and noise
median = cv.medianBlur(img,3)
cv.imshow("median",median)

#bilateral --> blur image with retain the edges
bilateral = cv.bilateralFilter(img,5,15,15) #5 --> Diameter of each pixel neighborhood that is used during filtering
#15 --> It controls how different the colors of the two pixels have to be before they are considered significantly different and influence the filtering process.
#15 --> It controls how far the pixel values will be filtered based on their spatial distance
cv.imshow("bilateral",bilateral)

cv.waitKey(0)