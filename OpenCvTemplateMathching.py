import numpy as np
import cv2

img = cv2.resize(cv2.imread('Assets/soccer_practice.jpg', 0), (0, 0), fx= 0.7, fy= 0.7)
template = cv2.resize(cv2.imread('Assets/shoe.PNG', 0), (0, 0), fx= 0.7, fy= 0.7)
# the shape is tuple that contains the height, the width, and optional the channels
h, w = template.shape

# 6 main methods to do templates, it means all the template methods 
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF, cv2.TM_CCOEFF_NORMED]

for method in methods:
    img2 = img.copy()

    # Perform convolution using matchTemplate method
    # This involves sliding the template over the image and comparing the template with each section of the image
    # The resulting 2d array will be composed by this --> (W - w + 1, H - h + 1)
    # For example if we have 4x4, 2x2 the result will be --> W = 4, w = 2, H = 4, h = 2 --> (3, 3) 
    # This is the number of times we can slide this image in x and y direction
    result = cv2.matchTemplate(img2, template, method)
    #(<min value in the array>, <max value in the array>, <min location in the array>, <max location in the array>)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    print(min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()