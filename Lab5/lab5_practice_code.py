# Lab 5 Histogram

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Grayscale histogram
# img = cv2.imread('../images/Eiffel_tower.jpg', 0)
#
#
# # Calculate the histogram
# hist = cv2.calcHist([img], [0], None, [256], [0, 256])
#
# # Plot the histogram
# plt.plot(hist)
# plt.title("Grayscale Histogram")
# plt.xlabel("Pixel intensity")
# plt.ylabel("Frequency")
# plt.show()

# # Color histogram
# img = cv2.imread('../images/Eiffel_tower.jpg')
# color = ('b', 'g', 'r')
#
# # Loop through each color channel (Blue, Green, Red)
# for i, col in enumerate(color):
#     # Calculate the histogram for each channel
#     hist = cv2.calcHist([img], [i], None, [256], [0, 256])
#     # Plot the histogram for the current channel
#     plt.plot(hist, color=col)
#
# plt.title("Color Histogram")
# plt.xlabel("Pixel Intensity")
# plt.ylabel("Frequency")
# plt.show()