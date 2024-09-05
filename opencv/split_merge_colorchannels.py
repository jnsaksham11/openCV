import cv2 as cv
import numpy as np

img =cv.imread('images/bg.png')
cv.imshow('image',img)

blank = np.zeros(img.shape[0:2],dtype='uint8')

b,g,r = cv.split(img) #b,g,r shows grayscale image with intensity difference

#this show corresponding color image
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)

# print(img.shape) 
# print(b.shape)
# print(g.shape)
# print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)


cv.waitKey(0)