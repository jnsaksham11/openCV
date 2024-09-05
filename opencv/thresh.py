import cv2 as cv
import numpy as np

img = cv.imread('images/cats.jpg')
cv.imshow("cats",img)

# img = cv.imread('images/cats.jpg',cv.IMREAD_GRAYSCALE)
# cv.imshow("cats",img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#simple thresholding
threshold , thresh = cv.threshold(gray,150,255, cv.THRESH_BINARY)
cv.imshow('threeshold',thresh)

threshold , thresh_inv = cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
cv.imshow('threeshold inverting',thresh_inv)

#adaptive thresholding
# adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,3)
# cv.imshow("adaptive threshold",adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,10) #adaptive_thresh_mean_c --> method for finding average of all surroundin intersities and    11 --> kernel size and 10--> subtract 10 from average and increase this value(10) more black
cv.imshow("adaptive threshold inverting",adaptive_thresh_inv)

adaptive_thresh_inv = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,10) 
cv.imshow("adaptive threshold inverting gaussian",adaptive_thresh_inv)

cv.waitKey(0)