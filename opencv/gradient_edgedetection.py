import cv2 as cv
import numpy as np

#Edge detection is the process of identifying the points in an image where the intensity or color changes abruptly. 
#These points typically correspond to object boundaries, texture boundaries, or discontinuities in the image.
#Edges are represented as a set of pixels or as a binary image where the edge pixels are marked as white (255) and the non-edge pixels are marked as black (0).

img = cv.imread('images/park.jpg')
cv.imshow('cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian",lap)

#sobel #cv,CV_64F --> 64 bit floating point ouput and 1,0 --> in x direction or 0,1 --> in y direction
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow("sobel x",sobelx)
cv.imshow("sobel y",sobely)
cv.imshow("combined sobel",combined_sobel)

#canny
canny = cv.Canny(gray,150,175)
cv.imshow("canny",canny)

cv.waitKey(0)