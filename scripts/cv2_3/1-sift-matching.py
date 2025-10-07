# Simple keypoint matching using K-Nearest neighbours.
# This code uses SIFT keypoints and descriptors but you can use any other 
# keypoint detector and/or descriptor:
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html

import numpy as np
import cv2
from matplotlib import pyplot as plt

# img1 = cv2.imread('data/flower.jpg',0)  # queryImage
# img2 = cv2.imread('data/flowers.jpg',0) # trainImage

#img1 = cv2.imread('data/monitor_rotated.jpg',0)  # queryImage
img1 = cv2.imread('data/plant_rotated.jpg',0)  # queryImage
img2 = cv2.imread('data/office.jpg',0) # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params (brute force)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = np.empty((img1.shape[0]+img2.shape[0], img1.shape[1]+img2.shape[1]), dtype=np.uint8)
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,img3,flags=2)

plt.imshow(img3),plt.show()
