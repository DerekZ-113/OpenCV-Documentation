# Week 8 OpenCV Lab 8: Edge Detection

## Code Files
- [lab8_sample_code.py](lab8_sample_code.py)
- [lab8 practice code.py](lab8_practice_code.py)

## 1. Introduction to Edge Detection
- **Edge Detection**: Identifies sharp discontinuities in an image, corresponding to significant changes in pixel intensity, often at object boundaries.
- **Applications**:
  - Object recognition
  - Image segmentation
  - Pattern recognition

## 2. Types of Edge Detection

### 2.1 Sobel Edge Detection
- **Definition**: Uses convolution kernels to calculate intensity gradients in horizontal and vertical directions.
- **Features**:
  - Provides both direction and magnitude of edges.
  - Simple and computationally efficient.
- **Pros**:
  - Fast and efficient.
  - Highlights edge orientation (horizontal, vertical, or diagonal).
- **Cons**:
  - Sensitive to noise.
  - Produces thicker edges.
- **Function**: `cv2.Sobel(src, ddepth, dx, dy, ksize)`
  - **Parameters**:
    - `src`: Source grayscale image.
    - `ddepth`: Depth of the destination image.
    - `dx`: Order of the derivative in x.
    - `dy`: Order of the derivative in y.
    - `ksize`: Kernel size (default 3).
- **Combining Results**:
  - Combine horizontal and vertical edges using:
    ```python
    sobel_combined = cv2.sqrt(sobel_x**2 + sobel_y**2)
    ```

```python
import cv2
import numpy as np

# Load image in grayscale
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges

# Combine Sobel X and Y
sobel_combined = cv2.sqrt(sobel_x**2 + sobel_y**2)

# Display the result
cv2.imshow("Sobel Edge Detection", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 2.2 Canny Edge Detection
- **Definition**: A multi-step process to detect a wide range of edges in images.
- **Steps**:
  1. Noise reduction using Gaussian blur.
  2. Gradient calculation.
  3. Non-maximum suppression.
  4. Double threshold.
  5. Edge tracking by hysteresis.
- **Pros**:
  - Accurate and robust.
  - Produces thin, well-defined edges.
  - Reduces noise.
- **Cons**:
  - Slower compared to Sobel.
  - Requires threshold tuning.
- **Function**: `cv2.Canny(image, threshold1, threshold2)`
  - **Parameters**:
    - `image`: Source grayscale image.
    - `threshold1`: Lower threshold for weak edges.
    - `threshold2`: Upper threshold for strong edges.

```python
import cv2

# Load image in grayscale
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display the result
cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 2.3 Sobel vs. Canny

| Feature              | Sobel                  | Canny                          |
|----------------------|------------------------|--------------------------------|
| Gradient Calculation | Intensity gradient     | Gradient with filtering        |
| Edge Detection       | Simple and fast        | More accurate and robust       |
| Noise Sensitivity    | Sensitive to noise     | Handles noise with Gaussian    |
| Edge Quality         | Thicker edges          | Thin, well-defined edges       |
| Control              | No thresholds          | User-defined thresholds        |

## 3. Additional Information and Insights

### 3.1 Understanding Gradients and Edge Detection
- **Gradients** represent changes in intensity across an image.
- **Horizontal vs Vertical Gradients**:
  - Sobel calculates gradients separately in both directions, allowing detection of edge orientation.
- **Gradient Magnitude**:
  - Combining horizontal and vertical gradients gives the overall strength of the edge.

### 3.2 Practical Use of Sobel
- **Use Case**:
  - Sobel is best suited for images with clear, simple edges (e.g., document images or basic shapes).
- **Tips**:
  - Preprocessing with Gaussian blur can reduce noise sensitivity.

### 3.3 Refinement with Canny
- **Key Steps**:
  - Noise Reduction: Gaussian blur minimizes high-frequency noise.
  - Gradient Calculation: Calculates edges more robustly than Sobel alone.
  - Double Thresholding:
    - Lower threshold ensures weak edges are considered if connected to strong ones.
    - Higher threshold ensures strong edges are always retained.
  - Fine-Tuning Thresholds:
    - Experiment with `threshold1` and `threshold2` to balance noise removal and edge detection accuracy.
    - For low-contrast images, lower both thresholds to detect edges clearly.

### 3.4 Comparison Summary
- **Sobel**:
  - Pros: Simplicity, speed, and directionality.
  - Cons: Thick edges, noise sensitivity.
- **Canny**:
  - Pros: Thin, precise edges with reduced noise.
  - Cons: Computationally intensive and requires threshold tuning.

## 4. Summary

### 4.1 Sobel Edge Detection
- Simple and fast.
- Effective for detecting horizontal and vertical edges in simple images.
- Produces thicker edges and is sensitive to noise.

### 4.2 Canny Edge Detection
- Advanced, multi-step process.
- Detects fine, detailed edges in complex images.
- Provides thinner, more defined edges.
- Requires experimenting with threshold values.
```