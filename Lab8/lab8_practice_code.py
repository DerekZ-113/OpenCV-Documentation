import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Load image in grayscale
image = cv2.imread('../images/Eiffel_tower.jpg', 0)

# # Sobel Edge Detection
# # Calculate gradients in horizontal and vertical directions
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges

# # Combine horizontal and vertical gradients
sobel_combined = cv2.sqrt(sobel_x**2 + sobel_y**2)

# # Display Sobel Edge Detection
# cv2.imshow("Sobel Edge Detection", sobel_combined)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Plot Sobel results
# plt.subplot(1, 3, 1)
# plt.imshow(sobel_x, cmap='gray')
# plt.title('Sobel X')

# plt.subplot(1, 3, 2)
# plt.imshow(sobel_y, cmap='gray')
# plt.title('Sobel Y')

# plt.subplot(1, 3, 3)
# plt.imshow(sobel_combined, cmap='gray')
# plt.title('Sobel Combined')

# plt.show()

# # Canny Edge Detection
# # Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# # Display Canny Edge Detection
# cv2.imshow("Canny Edge Detection", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Plot Canny results
# plt.imshow(edges, cmap='gray')
# plt.title('Canny Edge Detection')
# plt.show()