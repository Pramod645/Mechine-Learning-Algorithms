# find the canny edges in an image

# CHALLENGE: make a live edge detector with a webcam stream

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/flowers.jpg',0)
edges = cv2.Canny(img,100,150)  # vary the thresholds to see what happens

cv2.imshow('gray', img)
cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
