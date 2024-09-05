import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/cats.jpg')
cv.imshow("cats",img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)


masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)

#GRAYSCALE histogram 
# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
# gray_hist = cv.calcHist([gray],[0],masked,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram
colors = ('b','g','r')
for i,col in enumerate(colors):
    color_hist = cv.calcHist([img],[i],mask,[256],[0,256])
    #[i] --> In the case of a multi-channel color image (e.g., BGR), i can be [0], [1], and [2] for the Blue, Green, and Red channels, respectively.
    #[256] -->  the number of bins (histogram bins) for the histogram. It defines the number of intervals or subdivisions of the intensity range
    #[0,256] --> the range of pixel values over which the histogram will be computed. It's a tuple representing the minimum and maximum pixel values
    # plt.figure()
    plt.title('color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(color_hist, color = col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)