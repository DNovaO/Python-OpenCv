import cv2
import random

img = cv2.imread('Assets/apple_python.jpg',1)

#Coping and pasting parts of an image, slicing the img
# tag = img[500:700,600:900]
# img[100:300, 400:700] = tag

#Image representation
print("---------------------")
print(img) #Shows a numpy array
print("---------------------")
print(img[0]) #shows the rows pixel
print("---------------------")
print(img[257]) #show the rows pixel
print("---------------------")
print(img[257][45:400]) #show the rows pixel and shows pixels betwenn 45 and 400
print("---------------------")
print(type(img)) #Shows typeof, <class 'numpy.ndarray'>
print("---------------------")
print(img.shape) #Show values Red, Green, Blue but OpenCV uses BGR
print("---------------------")

#Manipulate the pixels to change their value(color)
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

        if (img[i][j] == [0, 0, 1]).all():
            print('Hi, Im white')

print("---------------------")
print(img[0]) #shows the rows pixel

#Shows window image
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()