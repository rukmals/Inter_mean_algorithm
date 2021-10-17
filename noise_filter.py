import numpy as np
import math
import cv2

def get_zero_array(W,H):
    zero_array = [([0]*H) for p in range(W)]
    return zero_array

def convolution(img, mask):
    size = len(mask)
    W = img.shape[0]-(size-1)
    H = img.shape[1]-(size-1)
    img_new = get_zero_array(W,H)
    for i in range(W):
        for j in range(H):
            x = 0
            for k in range(size):
                for l in range(size):
                    x = x + img[i+k][j+l]*mask[k][l]
            img_new[i][j]=x
    return img_new

def gaussian_filter(kernel_size,sigma):
    gau_filter = np.zeros((kernel_size , kernel_size))
    m = kernel_size//2
    n = kernel_size//2
    for x in range(-m, m+1):
        for y in range(-n, n+1):
            x1 = 2*np.pi*(sigma**2)
            x2 = np.exp(-(x**2 + y**2)/(2* sigma**2))
            gau_filter[x+m, y+n] = (1/x1)*x2
    return gau_filter

def convolution(img, mask):
    size = len(mask)
    W = img.shape[0]-(size-1)
    H = img.shape[1]-(size-1)
    img_new = get_zero_array(W,H)
    for i in range(W):
        for j in range(H):
            x = 0
            for k in range(size):
                for l in range(size):
                    x = x + img[i+k][j+l]*mask[k][l]
            img_new[i][j]=x
    return img_new