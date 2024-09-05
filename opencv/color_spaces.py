#color space --> a system that representing an array of pixel color for example rgb,greyspace,lamb,hsv etc
#open cv reads a images in BGR format and that's not the current system that we use to represent colors outside of opencv 
#outside the opencv we useds RBG format which is kind of inverse of BGR format
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/bg.png')
cv.imshow("images",img)

plt.imshow(img)
plt.show()

#bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

#bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("lab",lab)

#bgr to luv
luv = cv.cvtColor(img,cv.COLOR_BGR2Luv)
cv.imshow("luv",luv)

#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)
cv.imwrite("rgb.png",rgb)

plt.imshow(rgb)
plt.show()

#rgb,luv,lab,hsv,gray to bgr but hsv to lab
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("hsv_bgr",hsv_bgr)

#image[:,:,::-1]

cv.waitKey(0)
