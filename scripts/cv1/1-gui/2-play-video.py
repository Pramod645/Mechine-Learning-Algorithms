# stream a video file to screen

import numpy as np
import cv2

cap = cv2.VideoCapture('../data/output.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()