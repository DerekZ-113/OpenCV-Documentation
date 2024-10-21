# Week 4 OpenCV Lab 4: Image Processing

### Code Files
- [lab4_sample_code.py](lab4_sample_code.py)
- [lab4 practice code.py](lab4_practice_code.py)

## 1. Feature Detection and Matching

### 1.1 Harris Corner Detector (HCD)
- **Definition**: A corner detection operator used to extract corners and infer features of an image by analyzing the differential of the corner score.
- **Function**: `cv2.cornerHarris(src, dest, blockSize, kSize, freeParameter, borderType)`
  - **Parameters**:
    - `src`: Input image.
    - `dest`: Output image to store the Harris detector responses.
    - `blockSize`: Size of the neighborhood considered for corner detection.
    - `kSize`: Aperture parameter for the Sobel operator.
    - `freeParameter`: Harris detector parameter.
    - `borderType`: Pixel extrapolation method.

```python
import cv2

# Load an image
img = cv2.imread('building.jpg')

# Apply Harris Corner Detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dest = cv2.cornerHarris(gray, 2, 3, 0.04)

# Mark detected corners in the original image
img[dest > 0.01 * dest.max()] = [0, 0, 255]
```

### 1.2 SIFT (Scale-Invariant Feature Transform)
- **Definition**: Detects, describes, and matches local features in images, recognizing objects by comparing features in new images.
- **Function**: `sift = cv2.SIFT_create()` and `sift.detectAndCompute()`
  - **Usage**: SIFT finds distinct, invariant keypoints that are robust against scale, rotation, and illumination changes.

```python
# Create a SIFT object
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw keypoints on the original image
img_with_keypoints = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
```

## 2. Feature Matching

### 2.1 FLANN (Fast Library for Approximate Nearest Neighbors)
- **Definition**: An algorithm to match feature descriptors between images using approximate nearest neighbors.
- **Parameters**:
  - `algorithm`: Specifies the indexing algorithm (`FLANN_INDEX_KDTREE` for KD-tree).
  - `trees`: Number of trees used for KD-tree (higher value = slower but more accurate).
  - `search_params`: Controls search behavior (e.g., number of checks during search).

```python
# FLANN parameters
index_params = dict(algorithm=cv2.FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

# Perform KNN match
matches = flann.knnMatch(descriptors1, descriptors2, k=2)

# Apply Lowe's ratio test to filter good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)
```

## 3. Additional Information and Insights

### 3.1 Harris Corner Detector (HCD)
- **Concept**: 
  - Harris Corner Detector identifies corners by analyzing changes in intensity in all directions. It’s useful for tracking motion and detecting points of interest in images.
  
- **Usage Insights**:
  - The Harris response matrix marks high response values at corner regions. Thresholding helps identify these corners clearly, as shown with:
    ```python
    img[dest > 0.01 * dest.max()] = [0, 0, 255]  # Red marks on corners
    ```

- **Limitations**:
  - HCD is sensitive to noise. Applying **GaussianBlur** before corner detection can enhance performance:
    ```python
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    dest = cv2.cornerHarris(gray, 2, 3, 0.04)
    ```

### 3.2 SIFT (Scale-Invariant Feature Transform)
- **Concept**:
  - SIFT is a robust method to detect and describe local features that remain consistent under various transformations, such as scaling, rotation, or brightness changes.

- **Key Insights**:
  - **Keypoints** represent distinct image regions. **Descriptors** are vectors that describe these regions for comparison across images.
  
- **Example**:
  - Drawing keypoints using:
    ```python
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    ```
    This visualizes the detected keypoints with circles whose size reflects the scale of the keypoints.


### 3.3 FLANN (Fast Library for Approximate Nearest Neighbors)
- **Concept**:
  - FLANN is optimized for high-dimensional data and provides faster matching results, even with large datasets. It’s ideal for applications involving large-scale image retrieval or object detection.

- **How FLANN Works**:
  - **KD-tree**: Used as the indexing structure to speed up search operations.
  - **KNN Matching**: For every feature descriptor in one image, the `knnMatch()` function finds the k nearest neighbors in the other image.

- **Lowe's Ratio Test**:
  - Lowe’s test helps filter out ambiguous matches by checking the ratio between the distances of the closest and second-closest matches. This improves matching accuracy by removing weak matches.

- **Example Usage**:
  - Using `knnMatch()` with two descriptors:
    ```python
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)
    good_matches = [m for m, n in matches if m.distance < 0.7 * n.distance]
    ```
