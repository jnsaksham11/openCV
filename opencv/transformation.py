import cv2 as cv
import numpy as np

def translate(img,x,y):
    trans_mat= np.float32([[1,0,x],[0,1,y]]) # 2*3 matrix first row --> for x-axis(scale,shearing,translate) and second row --> for y axis(shearing,scale,translate)
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,trans_mat,dimensions)

    #-x --> left
    #-y --> up
    #x --> right
    #y --> down

def rotate(img,angle, rotpoint=None):
    (height,width) = img.shape[0:2]

    if rotpoint is None:
        rotpoint = (width//2,height//2)

    rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0) #generate 2*3 matrix --> (aboutrotatepoint,which angle,scalling factor) scale =1 means no change in size and shearing is zero--> no change in shearing
    dimensions=(width,height)

    return cv. warpAffine(img, rotmat,dimensions)

img = cv.imread('images/bg.png')
cv.imshow("image",img)

translated_image = translate(img,-100,100)
cv.imshow("translate",translated_image)

rotated_image = rotate(img,45)
cv.imshow("rotated",rotated_image)

# rotated_rotated_image = rotate(rotated_image,45)
# cv.imshow("rotate2",rotated_rotated_image)

#resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

#fliping
flip = cv.flip(img,0) # 0 --> along x axis and 1 --> along y axis and -1 --> along both x axix
cv.imshow("fliped",flip)

#cropping
cropped = img[200:500, 300:400]
cv.imshow("cropped",cropped)

cv.waitKey(0)

