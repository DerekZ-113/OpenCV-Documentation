# Week 10 OpenCV Lab 10: Camera

## Code Files
- [lab10_sample_code.py](lab10_sample_code.py)
- [lab10 practice code.py](lab10_practice_code.py)

## 1. Setting up Camera in OpenCV
- **Accessing Camera**: Use `cv2.VideoCapture()`
  - `0` for the default camera.
  - `1` for an external camera if connected.
- **Reading and Displaying Frames**:
  - Capture frames in a loop and display them.
  - Key functions:
    - `cap.read()`: Captures each frame.
    - `cv2.imshow("Camera Feed", frame)`: Displays the frame.
- **Releasing the Camera**:
  - Use `cap.release()` to release the camera resources after use.

## 2. Introduction to Optical Flow
- **Definition**: Tracks apparent motion of pixels between consecutive frames.
- **Applications**:
  - Motion detection
  - Feature tracking
- **Use Case in Lab**:
  - Motion detection
  - Feature tracking using two methods:
    - Lucas-Kanade (Sparse Optical Flow)
    - Dense Optical Flow

## 3. Motion Detection using Optical Flow

### 3.1 Lucas-Kanade Optical Flow (Sparse)
- **Method**: Tracks specified feature points across frames.
- **Strengths**:
  - Computationally efficient.
  - Accurate for small motions and specific points.
- **Weaknesses**:
  - Unsuitable for large motions.
  - Limited to specified points.
- **Function**:
  ```python
  cv2.calcOpticalFlowPyrLK(prev_frame, next_frame, prev_points, None, **params)
  ```
  - **Parameters**:
    - `prev_frame`: First frame in grayscale.
    - `next_frame`: Second frame in grayscale.
    - `prev_points`: Points to track (from `cv2.goodFeaturesToTrack`).
    - `params`: Parameters for the method.

### 3.2 Dense Optical Flow
- **Method**: Calculates motion vectors for all pixels in the frame.
- **Strengths**:
  - Captures detailed motion.
  - Suitable for large motions and scene-wide analysis.
- **Weaknesses**:
  - Computationally intensive.
  - Sensitive to noise.
- **Function**:
  ```python
  cv2.calcOpticalFlowFarneback(prev_frame, next_frame, None, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags)
  ```
  - **Parameters**:
    - `prev_frame`, `next_frame`: Consecutive frames in grayscale.
    - `pyr_scale`: Scale between pyramid levels.
    - `levels`: Number of pyramid levels.
    - `winsize`: Averaging window size.
    - `iterations`: Iterations at each level.
    - `poly_n`: Neighborhood size for polynomial expansion.
    - `poly_sigma`: Gaussian standard deviation for weighting.

## 4. Feature Tracking using Optical Flow
- **Shi-Tomasi Corner Detector**:
  - Detects stable features (corners) for tracking.
  - **Function**:
    ```python
    cv2.goodFeaturesToTrack(gray_frame, maxCorners, qualityLevel, minDistance)
    ```
    - **Parameters**:
      - `gray_frame`: Grayscale image.
      - `maxCorners`: Maximum number of corners.
      - `qualityLevel`: Minimum corner quality.
      - `minDistance`: Minimum distance between corners.
- **Integration with Lucas-Kanade**:
  - Pass detected features to `cv2.calcOpticalFlowPyrLK` to track them across frames.

## 5. Code Example
```python
import cv2
import numpy as np

# Set up camera
cap = cv2.VideoCapture(0)

# Parameters for Shi-Tomasi Corner Detection
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# Parameters for Lucas-Kanade Optical Flow
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Read the first frame
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Detect initial points to track
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# Create a mask for drawing
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Sparse Optical Flow: Lucas-Kanade
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
            frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)

    lk_output = cv2.add(frame, mask)

    # Dense Optical Flow: Farneback
    flow = cv2.calcOpticalFlowFarneback(old_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    hsv = np.zeros_like(frame)
    hsv[..., 1] = 255
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    dense_output = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Display the results
    cv2.imshow("Lucas-Kanade Optical Flow (Sparse)", lk_output)
    cv2.imshow("Dense Optical Flow", dense_output)

    # Update for next iteration
    old_gray = frame_gray.copy()
    if good_new is not None:
        p0 = good_new.reshape(-1, 1, 2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## 6. Additional Information and Insights

### 6.1 Lucas-Kanade Optical Flow
- Ideal for tracking specific points.
- Use cases: Object tracking in smaller, focused areas.

### 6.2 Dense Optical Flow
- Captures comprehensive motion across the frame.
- Useful for scene-wide motion analysis.

### 6.3 Visualization
- **Lucas-Kanade**: Tracks feature points with lines and circles.
- **Dense Optical Flow**: Visualizes motion direction (hue) and magnitude (value) using HSV color maps.

## 7. Summary

### 7.1 Camera Setup
- Use `cv2.VideoCapture` for real-time frame capture.
- Properly release the camera with `cap.release()`.

### 7.2 Optical Flow Methods
- **Lucas-Kanade**: Efficient, suitable for sparse points.
- **Dense Flow**: Detailed, scene-wide analysis.

### 7.3 Applications
- Motion detection.
- Feature tracking.
- Scene analysis.
