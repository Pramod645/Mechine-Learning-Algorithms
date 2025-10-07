# Sobel and Laplacian gradients with different data types.
# See important note on
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_gradients/py_gradients.html
# about setting output bit depth to avoid missing edges

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/sudoku.jpg',0)  # load as grayscale

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(3,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


# img = cv2.imread('../data/boxes.jpg',0)

# # Output dtype = cv2.CV_8U
# sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# # Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# abs_sobel64f = np.absolute(sobelx64f)
# sobel_8u = np.uint8(abs_sobel64f)

# plt.subplot(3,3,7),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,8),plt.imshow(sobelx8u,cmap = 'gray')
# plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,3,9),plt.imshow(sobel_8u,cmap = 'gray')
# plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()
