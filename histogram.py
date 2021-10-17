import matplotlib.pyplot as plt 
import cv2

image_name = input("Enter your image name for edge detection (should be save in the same location of the python file) like image_name.png/.jpg: ")
img = cv2.imread(image_name, 0 ) 

plt.hist(img.ravel(),256,[0,256])
plt.show()

# show the plotting graph of an image
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)
plt.show() 