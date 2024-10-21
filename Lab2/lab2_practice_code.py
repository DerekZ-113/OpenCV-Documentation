import cv2

# Load the image in color (original format)
# img = cv2.imread("../images/Eiffel_tower.jpg")
# cv2.imshow("Eiffel Tower", img)

# Load the image in grayscale
gray_eiffel = cv2.imread("../images/Eiffel_tower.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Gray Eiffel Tower", gray_eiffel)

# Save the image
# cv2.imwrite("gray_eiffel_tower.jpg", gray_eiffel)

# The window persist until a key is pressed
# waitKey parameter takes milliseconds before the window is destroyed
cv2.waitKey(0)
# Destroy all windows after exit the script
cv2.destroyAllWindows()