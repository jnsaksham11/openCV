import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle =cv.rectangle(blank.copy(), (30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)

#bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("bitwise and",bitwise_and)

#bitwise OR --> both region(pixels that high intensity between both images)
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise or",bitwise_or)

#bitwise XOR --> non-intersecting region
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise xor",bitwise_xor)

#bitwise NOT -->
bitwise_not1 = cv.bitwise_not(rectangle)
cv.imshow("bitwise not1",bitwise_not1)
bitwise_not2 = cv.bitwise_not(circle)
cv.imshow("bitwise not2",bitwise_not2)

cv.waitKey(0)