import numpy as np
import cv2

#Loading the webcam or the device with a camera
cap = cv2.VideoCapture(0)

#Looping until we press a key, this to get every camera frame
while True:
    #Return the frame, and tells if the capture actually work properly
    ret, frame = cap.read()

    #Getting the identificators for height and width, parseing to int.
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Image capture duplication (For Fun)
    image = np.zeros(frame.shape, np.uint8)

    #Resizing frame for multiple captures.
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    #Operation that slice the smaller frame
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    #Window to the capture
    cv2.imshow('Frame',image)

    #if we get a 'q' the capture will exit 
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()