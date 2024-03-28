# The idea is to convert the actual frame into a HSV color 
#Acronym Breakdown: RGB (red, green, blue), BGR (blue, green, red) and HSV (Hue saturation and Lightness/Brightness)
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    heitgth = int(cap.get(4))

    #this will take the image, take those RGB or BGR pixel values and convert them into an HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Now we pick an upperbound and a lowerbound
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #Create a mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #Convert al non blue pixels into dark pixels
    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame',result)
    cv2.imshow('mask',mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()