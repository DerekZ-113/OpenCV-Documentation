import cv2

img = cv2.imread("flower.png")

# gray_img = cv2.imread("flower.png", cv2.IMREAD_GRAYSCALE)

# week 2 codes
# cv2.imshow("flower_image", img)
# cv2.waitKey(0)
# cv2.waitKey(500)
# cv2.destroyAllWindows()
# cv2.imwrite("gray_flower.png", gray_img)

# week 3 codes
#resize
resized_img = cv2.resize(img, (300, 300))
cv2.imshow("resized image", resized_img)

#crop
cropped_img = img[80:200, 150, 330]
cv2.imshow("cropped image", cropped_img)

#rotate
rotated_img = img(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotated image", rotated_img)

#gray scale and HSV
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#draw shapes and text-line
print(img.shape) # to get height, width, channels of the image
cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 3)

cv2.waitKey(0)
cv2.destroyAllWindows()