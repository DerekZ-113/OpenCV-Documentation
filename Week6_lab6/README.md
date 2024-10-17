# Week 6 OpenCV Lab 6: Smoothing and Blurring

### Code Files
- [week6_lab6.py](week6_lab6.py)

## 1. Importance of Smoothing and Blurring
- **Smoothing and Blurring**: Essential image preprocessing techniques that reduce noise and detail in an image.
- **Applications**:
  - **Feature Extraction**: Simplifies images to make feature extraction more robust.
  - **Edge Detection**: Reduces noise, ensuring cleaner edge detection.
  - **Object Recognition**: Enhances image quality for better accuracy.

## 2. Types of Blurring Techniques

### 2.1 Averaging (Box Filter)
- **Definition**: The simplest method for blurring, replacing each pixel with the average of its neighboring pixels.
- **Function**: `cv2.blur(src, ksize)`
  - **Parameters**:
    - `src`: Input image.
    - `ksize`: Size of the kernel (e.g., `(5, 5)`) that determines the neighborhood size for averaging.

```python
import cv2
import matplotlib.pyplot as plt

# Apply averaging (box filter)
blurred_avg = cv2.blur(image, (5, 5))

# Display the blurred image
plt.imshow(blurred_avg)
plt.title("Averaging (Box Filter)")
plt.show()
```

### 2.2 Gaussian Blurring
- **Definition**: Uses a Gaussian function to smooth the image, preserving edges while reducing noise more effectively than averaging.
- **Function**: `cv2.GaussianBlur(src, ksize, sigmaX)`
  - **Parameters**:
    - `src`: Input image.
    - `ksize`: Kernel size (must be odd, e.g., `(5, 5)`).
    - `sigmaX`: Standard deviation in the X direction (set to `0` for automatic calculation).

```python
# Apply Gaussian blur
blurred_gauss = cv2.GaussianBlur(image, (5, 5), 0)

# Display the blurred image
plt.imshow(blurred_gauss)
plt.title("Gaussian Blurring")
plt.show()
```

### 2.3 Median Blurring
- **Definition**: Replaces the pixel value with the median of neighboring pixel values, effective for removing "salt-and-pepper" noise.
- **Function**: `cv2.medianBlur(src, ksize)`
  - **Parameters**:
    - `src`: Input image.
    - `ksize`: Kernel size (must be an odd number, e.g., `5`).

```python
# Apply median blur
blurred_median = cv2.medianBlur(image, 5)

# Display the blurred image
plt.imshow(blurred_median)
plt.title("Median Blurring")
plt.show()
```

### 2.4 Bilateral Filtering
- **Definition**: Smooths the image while preserving edges by considering both pixel intensity differences and spatial proximity.
- **Function**: `cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)`
  - **Parameters**:
    - `src`: Input image.
    - `d`: Diameter of the pixel neighborhood.
    - `sigmaColor`: Filter sigma in the color space (higher values result in more blurring).
    - `sigmaSpace`: Filter sigma in the coordinate space (higher values mean more spatial smoothing).

```python
# Apply bilateral filter
blurred_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Display the blurred image
plt.imshow(blurred_bilateral)
plt.title("Bilateral Filtering")
plt.show()
```

## 3. Summary

### 3.1 Averaging (Box Filter)
- Useful for basic noise reduction without caring about edge preservation.

### 3.2 Gaussian Blurring
- Preferred for smoother results with better edge preservation.

### 3.3 Median Blurring
- Effective for images with sharp noise, such as salt-and-pepper noise.

### 3.4 Bilateral Filtering
- Ideal when noise reduction is needed while preserving edges.

