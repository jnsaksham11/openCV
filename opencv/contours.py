import cv2 as cv
import numpy as np

#Contours are the outlines or boundaries of objects in an image. They represent the shape and structure of objects present in the image.
#Contours are typically represented as a list of points or as a sequence of points that define the perimeter of an object. Each contour is a closed curve that connects points of equal intensity or color.

img = cv.imread('images/cats.jpg')
cv.imshow("image",img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank",blank)

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grey",grey)

blur = cv.GaussianBlur(grey,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

canny = cv.Canny(blur,125,175)
cv.imshow("canny",canny)

# ret , thresh = cv.threshold(grey,125,255, cv.THRESH_BINARY)
# cv.imshow("thresh",thresh)

contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) # mod: cv.retr_list -->return all the contours in image , retr_external --> return only external contours and retr_tree --> return all contours that is in hierarchical system
#contour approximation method: cv.chain_approx_none does nothing and return all contours, cv.chain_approx_simple --> compresses all the quantities that are retured
print(f'{len(contours)}  contours is found')

cv.drawContours(blank,contours,-1,(0,255,0),1)
cv.imshow("contours",blank)

matrix1 = np.ones(img.shape,dtype='uint8') * 100
img_brighter = cv.add(img,matrix1)
cv.imshow("brightness",img_brighter)

img_darker = cv.subtract(img,matrix1)
cv.imshow("darker",img_darker)

matrix2 = np.ones(img.shape)* 0.8
img_contrast = np.uint8(cv.multiply(np.float64(img),matrix2))
cv.imshow("contrast",img_contrast)

cv.waitKey(0)