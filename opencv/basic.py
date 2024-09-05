import cv2 as cv

img = cv.imread('images/bg.png')

#converting to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#edge cascode
#Pixels with gradient values between the 125 and 175 thresholds are considered edges only if they are connected to high-gradient pixels.
#below 125 and large 175 not included in edges
canny = cv.Canny(blur,125,175)
cv.imshow("canny",canny)

#delating images --> morphological operation that expands regions of foreground pixels (white) in a binary image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("dilated",dilated)

#eroding --> morphological operation that shrinks regions of foreground pixels (white) in a binary image.
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("erode_images",eroded)

#resizing
resize = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resize)

#cropping the image
cropped = img[300:400,200:400]
cv.imshow("cropped",cropped)


cv.waitKey(0)