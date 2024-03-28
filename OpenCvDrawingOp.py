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

    #Variable to draw <source image, starting position, ending position, color, line thickness>
    img = cv2.line(frame, (0,0), (width,height), (255, 120, 0), 5)
    img = cv2.line(img, (0,height), (width,0), (255, 250, 0), 5)
    
    #Drawing figures
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128), -1)
    img = cv2.circle(img, (500,400), 50, (125,255,12), -1)

    #Drawing Texts
    font = cv2.FONT_ITALIC

    #Parameters <source image, text, center position, font, font scale, color, line thickness, line type>
    img = cv2.putText(img, 'Diego here!', (200,height-10), font, 2, (255, 255, 255), 5, cv2.LINE_AA)

    #Window to the capture
    cv2.imshow('Frame',img)

    #if we get a 'q' the capture will exit 
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()