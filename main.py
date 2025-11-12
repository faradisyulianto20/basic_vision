import cv2
import numpy as np

img = cv2.imread('apple.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

mask = cv2.medianBlur(mask, 5)

cv2.imwrite('mask_apel.png', mask)

cv2.imshow('Mask', mask)
cv2.waitKey(0)

cv2.destroyAllWindows()
