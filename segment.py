# https://www.analyticsvidhya.com/blog/2019/04/introduction-image-segmentation-techniques-python/

from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

## Region-based Segmentation ##

image = plt.imread('1.jpeg')
# print(image.shape)
# plt.imshow(image)

# Convert Image into grayscale
gray = rgb2gray(image)
# plt.imshow(gray, cmap='gray')

# It flattens the image
gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
# print(gray,gray.shape)
# print(gray_r, gray_r.shape)

for i in range(gray_r.shape[0]):
    # Make two segments using mean of the pixel value
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 3
    # elif gray_r[i] > 0.5:
    #     gray_r[i] = 2
    # elif gray_r[i] > 0.25:
    #     gray_r[i] = 1
    else:
        gray_r[i] = 0
# Make it into an image again
gray = gray_r.reshape(gray.shape[0], gray.shape[1])
# cmap => color map, it gives color 
plt.imshow(gray, cmap='gray')
plt.show()

## Edge Detection Segmentation ##
image = plt.imread('index.png')