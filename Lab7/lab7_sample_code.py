import cv2
import numpy as np
import matplotlib.pyplot as plt


# # Load image in grayscale
image = cv2.imread('../images/flower.png', 0)
#
# # Simple thresholding
# # Apply simple thresholding
# _, thresh_simple = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#
# # Show the image
# plt.imshow(thresh_simple, cmap = 'gray')
# plt.title('Simple Thresholding')
# plt.show()


# # Apply adaptive thresholding
# thresh_adaptive_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#
# # Apple adaptive Gaussian thresholding
# thresh_adaptive_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#
# # Show both results
# plt.subplot(1, 2, 1)
# plt.imshow(thresh_adaptive_mean, cmap='gray')
# plt.title('Adaptive Mean Thresholding')
#
# plt.subplot(1,2, 2)
# plt.imshow(thresh_adaptive_gaussian, cmap='gray')
# plt.title('Adaptive Gaussian Thresholding')
#
# plt.show()

# # Otsu's Binarization
# # Apply Otsu's binarization
# _, thresh_ostu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
# # Show the result
# plt.imshow(thresh_ostu, cmap='gray')
# plt.title('OTSU')
# plt.show()