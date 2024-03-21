import cv2

#Image declaration, resize and rotation
img = cv2.imread('Assets/apple_python.jpg',0)
img = cv2.resize(img,(0,0), fx=0.5,fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

#Overwriting new image.jpg with the atributes of modified original img
cv2.imwrite('new_img.jpg',img)

#Window to show image, and closes until user close it.
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()