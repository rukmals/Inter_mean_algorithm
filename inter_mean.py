import numpy as np
import math
import cv2
from noise_filter import gaussian_filter , convolution

# select forground as white and background as black
def inter_mean_segmentation(img , threshold , num_iterations):
    zero_list = np.zeros(img.shape)
    for iter in range(num_iterations):
        r1 = []
        r2 = []
        print(threshold)
        for i in range(zero_list.shape[0]):
            for j in range(zero_list.shape[1]):
                if img[i][j]>=threshold:
                    zero_list[i][j] = 0 
                    r1.append(img[i][j])
                else:
                    zero_list[i][j] = 255 
                    r2.append(img[i][j])
        m1 = (sum(r1)/len(r1))
        m2 = (sum(r2)/len(r2))
        threshold = (m1+m2)//2
        print("mean r1 : ",m1)
        print("mean r2 : ",m2)
    return zero_list


if __name__ == '__main__':
    print("........Read Image..........")
    image_name = input("Enter your image name for edge detection (should be save in the same location of the python file) like image_name.png/.jpg: ")
    img = cv2.imread(image_name,0) # open image in gray scale

    # Gaussian filter for noise filtering
    print("........Start Gaussain Filtering..........")
    kernel_size = int(input("Enter your Gaussian Kernel Size: "))
    sigma = int(input("Enter Sigma value for Gaussian Filer : "))
    kernel = gaussian_filter(kernel_size,sigma)
    gaussian_img = convolution(img ,kernel)
    noise_filtered_image = np.array(gaussian_img)

    print("........Start Segmentation..........")
    tr = int(input("Enter the Initial Threshold Value selecting from Histogram (use histohram.py file for this ): "))
    itr = int(input("Enter the number of steps you want to run the inter mean algorithm : "))
    segmented_img = inter_mean_segmentation(noise_filtered_image , tr , itr)
    output_name = 'segmented_'+image_name
    cv2.imwrite(output_name,segmented_img)