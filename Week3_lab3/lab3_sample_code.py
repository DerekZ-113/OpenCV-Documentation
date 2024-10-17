import cv2

img = cv2.imread("../images/flower.png")

#resize
# resized_img = cv2.resize(img, (300, 300))
# cv2.imshow("resized image", resized_img)

# #crop
# cropped_img = img[80:200, 150, 230]
# cv2.imshow("cropped image", cropped_img)
#
# #rotate
# rotated_img = img(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.imshow("rotated image", rotated_img)
#
# #gray scale and HSV
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# draw shapes and text-line
# print(img.shape) # to get height, width, channels of the image
# rectangle = cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 3, 3)
# cv2.imshow("rectangle", rectangle)
#
# draw a line
# line_img = cv2.line(img, (100, 100), (200, 200), (255, 0, 0), 3)
# cv2.imshow("line", line_img)
#
# put text on image
# text_img = cv2.putText(img, "Hello", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2 )
# cv2.imshow("text", text_img)

# draw a circle
circle_img = cv2.circle(img,(100,100),100,(0,255,0),4)
cv2.imshow("Circle", circle_img)

cv2.waitKey(0)
cv2.destroyAllWindows()