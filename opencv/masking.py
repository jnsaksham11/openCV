import cv2 as cv
import numpy as np

img = cv.imread('images/cats 2.jpg')
cv.imshow('cats',img)

#same size of mask and image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank", blank)

mask1 = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("mask1",mask1)

mask2 = cv.rectangle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+100,img.shape[0]//2 + 100),255,-1)
cv.imshow("mask2",mask2)

masked = cv.bitwise_and(img,img,mask=mask1)
cv.imshow('masked',masked)

cv.waitKey(0)