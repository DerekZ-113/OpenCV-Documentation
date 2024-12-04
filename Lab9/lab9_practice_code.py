import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load and preprocess the image
image = cv2.imread('../images/Eiffel_tower.jpg', 0)  # Replace with the correct path to the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale

# # Simple thresholding for binary conversion
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# # Find contours using the binary image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Drawing contours on the original image
# # Draw all contours (-1 specifies all contours)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# # Display the contours using OpenCV
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Display contours using Matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Contours')
plt.show()

# # Exploring different contour retrieval modes
# contours_list, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# contours_tree, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Draw contours for specific retrieval modes if needed
# cv2.drawContours(image, contours_list, -1, (255, 0, 0), 2)  # Blue for RETR_LIST
# cv2.drawContours(image, contours_tree, -1, (0, 0, 255), 2)  # Red for RETR_TREE