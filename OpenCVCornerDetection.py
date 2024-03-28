import numpy as np
import cv2

img = cv2.imread('Assets\Chess_Board.svg.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# Convert the image into gray scale, for easy detection, applies for every image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Introducing algorithms for edges, features and corners detection
# AKA Shi-Tomasi Corner Detector
# Parameter of the function are:
# (<image or videocapture>,< # Of corners we want to return or the best corners to return>, <Pick the quality of our corners (0-1)>, <minimum euclidean distance between corners that are return>)
# This means if the image have 5000 hypotetical corners it will return the best 100 corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# Return float type corners
# print(corners)
# Convert the float into integers to draw the corners in the correct way
corners = np.int0(corners)

# Drawing circles in every corner we detect
for corner in corners:
    #This flat all in an array, so this remove all the interior rents ([[0, 1, 2]]) --> [0, 1, 2]  [[1, 2], [2, 1]] --> [1, 2, 2, 1]
    x, y = corner.ravel()
    #now we draw the corners with the coordinates 
    cv2.circle(img, (x,y), 5, (255, 0, 0), -1)

#Drawing lines between every corner with a different color
for i in range(len(corners)):
    for j in range(i + 1,len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        # We use a lambda function or anonymous function to work with full integers of python and not numpy typeof integers
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)



cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()