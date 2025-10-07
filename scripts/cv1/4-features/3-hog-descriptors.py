import cv2
img = cv2.imread('../data/flowers.jpg')

winSize = (64,64)
blockSize = (16,16)
blockStride = (8,8)
cellSize = (8,8)
nbins = 9
derivAperture = 1
winSigma = 4.
histogramNormType = 0
L2HysThreshold = 2.0000000000000001e-01
gammaCorrection = 0
nlevels = 64
hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins,
	derivAperture, winSigma, histogramNormType, L2HysThreshold,
	gammaCorrection, nlevels)

winStride = (8,8)
padding = (8,8)
locations = ((10,20),)
hist = hog.compute(img,winStride,padding,locations)

'''
The resultant hog descriptor will have dimensions: 9 orientations X (4 corner
blocks that get 1 normalization + 6x4 blocks on the edges that get 2
normalizations + 6x6 blocks that get 4 normalizations) = 1764, since we have 
given only one location to hog.compute(): (10,20).

If you want more locations then add them to the tuple above.

Note that the result is a vector so you can pass it to a classifier as a feature
to work with.
'''

print(hist.shape)
