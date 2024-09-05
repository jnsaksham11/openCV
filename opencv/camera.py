import sys
import cv2 as cv

s=0
if len(sys.argv)>1:
    s = sys.argb[1]

image_filter="preview"
alive = True
source =cv.VideoCapture(s)

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break
    
    if image_filter == "preview":
        result = frame
    elif image_filter == "canny":
        result = cv.Canny(frame,80,175)
    elif image_filter == "blur":
        result = cv.GaussianBlur(frame,(7,7),0)
    elif image_filter =="gray":
        result = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    elif image_filter =="rgb":
        result = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    elif image_filter =="filter":
        result = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    cv.imshow("camera",result)

    key = cv.waitKey(1)
    if key == ord('q') or key ==27:
        alive =False
    elif key ==ord('c'):
        image_filter = "canny"
    elif key == ord('b'):
        image_filter = "blur"
    elif key == ord('p'):
        image_filter = "preview"
    elif key == ord('g'):
        image_filter="gray"
    elif key == ord('i'):
        image_filter = "rgb"
    elif key == ord('f'):
        image_filter = "filter"

source.release()
cv.destroyAllWindows()