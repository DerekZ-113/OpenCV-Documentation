import cv2

img = cv2.imread("flower.png")

gray_img = cv2.imread("flower.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("flower_image", img)

# cv2.waitKey(0)

# cv2.waitKey(500)

# cv2.destroyAllWindows()

cv2.imwrite("gray_flower.png", gray_img)