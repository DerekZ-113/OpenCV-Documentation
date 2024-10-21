# Week 7 OpenCV Lab 7: Thresholding

### Code Files
- [week7_lab7.py](week7_lab7.py)

## 1. Introduction to Thresholding
- **Thresholding**: A simple image segmentation technique that converts a grayscale image into a binary image.
- **Types of Thresholding Covered**:
  - **Simple Thresholding**
  - **Adaptive Thresholding**
  - **Otsu's Binarization**

## 2. Types of Thresholding

### 2.1 Simple Thresholding
- **Definition**: A fixed threshold value is used for the entire image; each pixel is compared to this value and assigned a binary value.
- **Pros**: Easy to implement, works well for uniform lighting.
- **Cons**: Not effective for images with varying lighting conditions.
- **Function**: `cv2.threshold(src, thresh, maxval, type)`
  - **Parameters**:
    - `src`: The source grayscale image.
    - `thresh`: The threshold value.
    - `maxval`: Value to assign to pixels exceeding the threshold.
    - `type`: Type of thresholding to apply (e.g., `cv2.THRESH_BINARY`).

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply simple thresholding
_, thresh_simple = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Show the image
plt.imshow(thresh_simple, cmap='gray')
plt.title('Simple Thresholding')
plt.show()
```

### 2.2 Adaptive Thresholding
- **Definition**: Threshold value is calculated for smaller regions of the image, making it effective for varying lighting conditions.
- **Types**:
  - **Mean Adaptive Thresholding**: Threshold is the mean of the neighborhood values minus a constant.
  - **Gaussian Adaptive Thresholding**: Threshold is the weighted sum of the neighborhood values minus a constant.
- **Pros**: Handles varying lighting, robust.
- **Cons**: Slower compared to simple thresholding.
- **Function**: `cv2.adaptiveThreshold(src, maxval, adaptiveMethod, thresholdType, blockSize, C)`
  - **Parameters**:
    - `src`: The source grayscale image.
    - `maxval`: Value to assign to pixels exceeding the threshold.
    - `adaptiveMethod`: Method for calculating threshold (`cv2.ADAPTIVE_THRESH_MEAN_C` or `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`).
    - `thresholdType`: Type of thresholding to apply (e.g., `cv2.THRESH_BINARY`).
    - `blockSize`: Size of neighborhood area used to calculate the threshold (must be odd).
    - `C`: Constant subtracted from the mean or weighted mean.

```python
# Apply adaptive mean thresholding
thresh_adaptive_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply adaptive Gaussian thresholding
thresh_adaptive_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Show both results
plt.subplot(1, 2, 1), plt.imshow(thresh_adaptive_mean, cmap='gray')
plt.title('Adaptive Mean Thresholding')
plt.subplot(1, 2, 2), plt.imshow(thresh_adaptive_gaussian, cmap='gray')
plt.title('Adaptive Gaussian Thresholding')
plt.show()
```

### 2.3 Otsu's Binarization
- **Definition**: Automatically calculates the optimal threshold value based on the image's histogram to minimize variance between foreground and background.
- **Pros**: Automatic thresholding, effective for images with bimodal histograms.
- **Cons**: Not effective for complex histograms or uneven lighting.
- **Function**: `cv2.threshold(src, thresh, maxval, type + cv2.THRESH_OTSU)`
  - **Parameters**:
    - `src`: The source grayscale image.
    - `thresh`: Set to 0, as Otsu's method determines the threshold automatically.
    - `maxval`: Value to assign to pixels exceeding the threshold.
    - `type`: Thresholding method combined with `cv2.THRESH_OTSU`.

```python
# Apply Otsu's binarization
_, thresh_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Show the result
plt.imshow(thresh_otsu, cmap='gray')
plt.title("Otsu's Binarization")
plt.show()
```

## 3. Summary

### 3.1 Simple Thresholding
- Best for images with uniform lighting.

### 3.2 Adaptive Thresholding
- Handles images with varying lighting but is slower.

### 3.3 Otsu's Binarization
- Effective for images with clear intensity separation but struggles with uneven lighting or complex histograms.

## 4. Additional Information and Insights

### 4.1 Simple Thresholding: When and How to Use

- **Concept**:
  - Simple thresholding assigns a binary value to each pixel based on a fixed threshold value.

- **Use Cases**:
  - Ideal for documents or images with clear foreground and background separation.

### 4.2 Adaptive Thresholding: Best Practices

- **Concept**:
  - Adaptive thresholding calculates the threshold for smaller regions (blocks) of the image, making it more effective for varying lighting conditions.

- **When to Use**:
  - Ideal for real-world applications like license plate recognition or document scanning where lighting conditions are not uniform.

- **Methods**:
  - **Adaptive Mean Thresholding**: Works well for moderate lighting variations.
  - **Adaptive Gaussian Thresholding**: Better for more complex lighting patterns due to its weighted averaging.

### 4.3 Otsu's Binarization: Practical Use

- **Concept**:
  - Otsu's method calculates the optimal threshold by minimizing the intra-class variance (variance within the background and foreground).

- **Applications**:
  - Best suited for images with a bimodal histogram (two distinct peaks representing foreground and background intensities).

- **Limitations**:
  - Struggles with complex histograms where there are more than two significant intensity levels or where lighting is not uniform.

- **Combining Otsu's with Gaussian Blur**:
  - Applying a Gaussian blur before Otsu's binarization can improve results by smoothing out noise:
    ```python
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    _, thresh_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.imshow(thresh_otsu, cmap='gray')
    plt.title("Otsu's Binarization with Gaussian Blur")
    plt.show()
    ```