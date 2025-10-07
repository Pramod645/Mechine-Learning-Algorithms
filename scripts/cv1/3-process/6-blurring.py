# various convolutions on images

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/lion.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imshow('original', img)

## Average filter over 5x5 grid
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
#OR
# dst = cv2.blur(img, (5,5))
cv2.imshow('average filter', dst)

## Gaussian
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('gaussian blur', blur)


## Median filter
noisy = cv2.imread('../data/noisy2.png')
median = cv2.medianBlur(noisy,5)
cv2.imshow('noisy image', noisy)
cv2.imshow('median filter', median)


## Bilateral filter (preserves edges but smoothes texture)
blur = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('bilateral filter', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
