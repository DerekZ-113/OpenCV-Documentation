import cv2

# Load the image in color (original format)
img = cv2.imread("../images/flower.png")
# cv2.imshow("flower_image", img)

# Load the image in grayscale
gray_img = cv2.imread("../images/flower.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("flower_gray", gray_img)

# Save the image
# cv2.imwrite("gray_flower.png", gray_img)

# The window persist until a key is pressed
# waitKey parameter takes milliseconds before the window is destroyed
cv2.waitKey(0)
# Destroy all windows after exit the script
cv2.destroyAllWindows()