# Image Processing
import cv2
import numpy as np

# Part 1: Harris Corner Detection
image = cv2.imread('../images/desk1.JPG')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Harris Corner Detection
# gray = np.float32(gray)
# harris_corners = cv2.cornerHarris(gray, 5, 3, 0.04)
# #
# # # Dilate the detected corners to enhance them
# harris_corners = cv2.dilate(harris_corners, None)
# #
# # # Threshold for an optimal value
# image[harris_corners >= 0.01 * harris_corners.max()] = [0, 0, 255]
#
# # Show the image with detected corners
# cv2.imshow('Harris Corners', image)


# # Part 2: SIFT Detector
# sift = cv2.SIFT_create()
# keypoints, descriptors = sift.detectAndCompute(gray, None)
#
# # Draw keypoints
# image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
# # Show the image with detected keypoints
# cv2.imshow('SIFT', image_with_keypoints)


# # Part 3 Feature Matching with FLANN
image1 = cv2.imread('../images/desk1.JPG', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('../images/desk2.JPG', cv2.IMREAD_GRAYSCALE)
#
# # SIFT Detector
sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)
#
# # FLANN Matcher
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(descriptors1, descriptors2, k=2)
#
# # Apply ratio test as per Lowe's paper
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)
#
# # Draw matches
result = cv2.drawMatches(image1, keypoints1, image2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow("Feature Matching", result)
#
#
#
cv2.waitKey(0)
cv2.destroyAllWindows()