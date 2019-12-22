# https://opencv-python.readthedocs.io/en/latest/doc/15.imageContours/imageContours.html

import cv2
import numpy as np

img = cv2.imread('./1.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray,127,255,0) # change binary

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()