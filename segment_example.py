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

# converting to grayscale
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
# # Make it into an image again
# gray = gray_r.reshape(gray.shape[0], gray.shape[1])
# # cmap => color map, it gives color 
# plt.imshow(gray, cmap='gray')
# plt.show()

## Edge Detection Segmentation ##
image = plt.imread('index.png')

gray = rgb2gray(image)

# defining the sobel filters
sobel_horizontal = np.array([np.array([1, 2, 1]), np.array([0, 0, 0]), np.array([-1, -2, -1])])
print(sobel_horizontal, 'is a kernel for detecting horizontal edges')

sobel_vertical = np.array([np.array([-1, 0, 1]), np.array([-2, 0, 2]), np.array([-1, 0, 1])])
print(sobel_vertical, 'is a kernel for detecting vertical edges')

# convolve this filter over the image using the convolve function of the ndimage package from scipy
out_h = ndimage.convolve(gray, sobel_horizontal, mode='reflect')
out_v = ndimage.convolve(gray, sobel_vertical, mode='reflect')
# here mode determines how the input array is extended when the filter overlaps a border.

# plt.imshow(out_h, cmap='gray')
# plt.imshow(out_v, cmap='gray')

# laplace operatro( detect both horizontal and vertical edges at the same time )

kernel_laplace = np.array([np.array([1, 1, 1]), np.array([1, -8, 1]), np.array([1, 1, 1])])
print(kernel_laplace, 'is a laplacian kernel')

out_l = ndimage.convolve(gray, kernel_laplace, mode='reflect')
# plt.imshow(out_l, cmap='gray')
# plt.show()


## Image Segmentation based on Clustering ##
pic = plt.imread('1.jpeg')/255 # dividing by 255 to bring the pixel values between 0 and 1
print(pic.shape)
# plt.imshow(pic)
# plt.show()

# For clustering the image using k-means, we first need to convert it into a 2-dimensional array whose shape will be (length*width, channels)
pic_n = pic.reshape(pic.shape[0]*pic.shape[1], pic.shape[2])
print(pic_n.shape)

# The cluster_centers_function of k-means will return the cluster centers and labels_function will give us the label for each pixel
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5, random_state=0).fit(pic_n)
pic2show = kmeans.cluster_centers_[kmeans.labels_]

# Bring back the clusters to their original shape(3-dimensional image)
cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])
plt.imshow(cluster_pic)
plt.show()