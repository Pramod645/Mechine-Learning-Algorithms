import cv2
import numpy as np

img = cv2.imread('../data/einstein.jpg')
rows,cols,_ = img.shape
# cv2.imshow('original', img)



## SCALING
##
res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
#OR
# height, width = img.shape[:2]
# res = cv2.resize(img,(0.5*width, 0.5*height), interpolation = cv2.INTER_CUBIC)
# cv2.imshow('resized', res)



## TRANSLATION
##
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('translated', dst)



## ROTATION
##
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('rotated', dst)



## AFFINE TRANSFORM
## (preserves parallel lines, needs three points to match in each image plane)
img = cv2.imread('../data/grid.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('grid original', img)
# cv2.imshow('grid affine', dst)



## PROJECTIVE TRANSFORM
## (preserves lines, needs four points to match in each image plane)
img = cv2.imread('../data/sudoku.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
cv2.imshow('sudoku original', img)
cv2.imshow('sudoku aligned', dst)



cv2.waitKey(0)
cv2.destroyAllWindows()

