import cv2 as cv
import numpy as np

#draw a blank image
blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow("blank",blank)

# #paint a image
# blank[200:500,200:300] = 0,0,250 #200 to 500 y and 200 to 300 x and 
# cv.imshow("red",blank)

#draw a rectangle
# cv.rectangle(blank,(5,5),(250,400),(0,250,0),thickness=2)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,250,0),thickness=cv.FILLED) #thickness = -1
# cv.imshow("rectangle",blank) 

#draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,0,250),thickness=-1)
# cv.imshow("with circle also",blank)

#draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(250,250,250),thickness=5)
# cv.imshow("with line also",blank)

# draw a text
# cv.putText(blank,"hello my name is lakhan",(250,250),cv.FONT_HERSHEY_TRIPLEX,1,(255,0,0))
cv.putText(blank,"hello my name is lakhan",(0,200),cv.FONT_HERSHEY_TRIPLEX,1,(255,0,0)) # (0,200) --> bottom left
cv.imshow("text",blank)

cv.waitKey(0)
