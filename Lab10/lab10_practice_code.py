import cv2
import numpy as np

# # Setting up the camera
cap = cv2.VideoCapture(0)  # 0 for the default camera; 1 for an external camera

# Parameters for Shi-Tomasi Corner Detection
feature_params = dict(maxCorners=200, qualityLevel=0.3, minDistance=7, blockSize=7)

# Parameters for Lucas-Kanade Optical Flow
lk_params = dict(winSize=(20, 20), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Read the first frame from the camera
ret, old_frame = cap.read()
if not ret:
    print("Failed to grab frame. Exiting.")
    cap.release()
    exit()

old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Detect initial feature points using Shi-Tomasi Corner Detection
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# Create a mask for drawing tracks
mask = np.zeros_like(old_frame)

while True:
    # Capture the next frame
    ret, frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # Lucas-Kanade Optical Flow (Sparse)
    # Calculate optical flow using Lucas-Kanade method
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select good points
    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Draw the tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
            frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)

        # Overlay the tracks on the original frame
        lk_output = cv2.add(frame, mask)

    # Display the sparse optical flow
    cv2.imshow("Lucas-Kanade Optical Flow (Sparse)", lk_output)

    # # Dense Optical Flow
    # Calculate dense optical flow using Farneback method
    flow = cv2.calcOpticalFlowFarneback(old_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Convert flow to HSV format for visualization
    hsv = np.zeros_like(frame)
    hsv[..., 1] = 255
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    dense_output = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Display the dense optical flow
    cv2.imshow("Dense Optical Flow", dense_output)

    # Update the previous frame and points
    old_gray = frame_gray.copy()
    if p1 is not None:
        p0 = good_new.reshape(-1, 1, 2)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()