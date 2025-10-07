# Find and mark the lines in an image with Hough algorithm

import cv2
import numpy as np

img = cv2.imread('../data/sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find the Canny edges we will search for lines
edges = cv2.Canny(gray,50,150,apertureSize = 3)

# find the Hough lines
lines = cv2.HoughLines(edges,1,np.pi/180,200)
for line in lines:
	for rho,theta in line:
	    a = np.cos(theta)
	    b = np.sin(theta)
	    x0 = a*rho
	    y0 = b*rho
	    x1 = int(x0 + 1000*(-b))
	    y1 = int(y0 + 1000*(a))
	    x2 = int(x0 - 1000*(-b))
	    y2 = int(y0 - 1000*(a))

	    # draw them on the image
	    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Hough lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
