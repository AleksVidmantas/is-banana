import cv2
import numpy

print("Is Banana?")
img = cv2.imread('banana.jpg',0)
cv2.imshow('banana.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
