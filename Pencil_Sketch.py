# Description : Program to convert Image to Pencil Sketch
'''
Data Science Intern at Let's Grow More LGMVIP Sept 22
Beginner Level Task
Image to Pencil Sketch with Python
Anish Dhondi
'''
#Importing cv2 module
import cv2

#Getting the Image Location and Image
img_location = 'C:/Users/Anish Mithil/OneDrive/Desktop/'
filename = '1.jpg'

#Read the image
img = cv2.imread(img_location+filename)

#Convert the img to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Invert the Img
inverted_gray_image = 255 - gray_img

#blur the img by gaussian function
blurred_img = cv2.GaussianBlur(inverted_gray_image,(21,21),0)

#Invert the Blurred Image
inverted_blurred_image = 255 - blurred_img

#Creating the Pencil sketch Image
pencil_sketch_IMG = cv2.divide(gray_img,inverted_blurred_image, scale=256.0 )

cv2.imshow('Original image',img)
cv2.imshow('New image',pencil_sketch_IMG)
cv2.waitKey(0)


