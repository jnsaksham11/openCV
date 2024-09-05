import cv2 as cv

#function for images,existing video and live video
def rescale_frame(frame, scale):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)

    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA) #interpolation: refers to the method used to estimate the values of pixels at non-grid positions when resizing or transforming an image.


#reading images
img = cv.imread('images/pxfuel.jpg') #This function is used to read an image file from disk into a NumPy array.

resize_image = rescale_frame(img,0.1)

cv.imshow('window_name',img) #This function is used to display an image in a window.
cv.imshow("resize",resize_image)

cv.waitKey(0) #This function waits for a key press in the window specified  or fuction return asci code for keboard inputs

#reading videos
capture = cv.VideoCapture('images/dog.mp4') #creates a video capture object(instance of class videocaptue()), which is used to capture video frames from a video file or a camera device.
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))

#create a video writer object with output file name and fourcc code and fps and dimension and color_bool
out_avi = cv.VideoWriter('dog.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10.0, (frame_width, frame_height), None)


while True:
    istrue, frame = capture.read() # reads a single frame from the video capture object. A boolean indicating whether the frame was successfully read. The actual frame data, stored as a NumPy array.

    frame_resize = rescale_frame(frame,0.75)

    cv.imshow("video_read", frame)
    cv.imshow("resize",frame_resize)

    out_avi.write(frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

out_avi.release()
capture.release() #release the capture object
cv.destroyAllWindows() #destroy all window which is shown by cv
    

