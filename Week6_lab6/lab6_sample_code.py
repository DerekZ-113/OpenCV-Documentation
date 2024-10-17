# Lab 6 Smoothing and Blurring

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../images/Eiffel_tower.jpg')

# Averaging
# blurred = cv2.blur(img, (5, 5))
# plt.imshow(img)
# plt.title('Averaging (Box Filter)')
# plt.show()

# Gaussian Blurring
# blurred_guass = cv2.GaussianBlur(img, (5, 5), 0)
# plt.imshow(blurred_guass)
# plt.title('Gaussian Blurred Image')
# plt.show()

# Median Blurring
# blurred_median = cv2.medianBlur(img, 5)
# plt.imshow(blurred_median)
# plt.title("Median Blurred Image")
# plt.show()

# Bilateral Filter
blurred_bilateral = cv2.bilateralFilter(img, 9, 75, 75)
plt.imshow(blurred_bilateral)
plt.title("Bilateral filter")
plt.show()