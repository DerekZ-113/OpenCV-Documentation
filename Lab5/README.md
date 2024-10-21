# Week 5 OpenCV Lab 5: Histogram

### Code Files
- [week5_lab5.py](week5_lab5.py)

## 1. Introduction to Histograms
- **Histogram**: A graphical representation showing the frequency of pixel intensity values in an image.
- **Pixel Intensity**: Ranges from 0 (black) to 255 (white) for grayscale images.
- **Usage**: Histograms help understand how pixel intensities are distributed across an image, aiding in tasks like image thresholding, contrast adjustment, and object detection.

## 2. Types of Histograms

### 2.1 Grayscale Histogram
- **Definition**: Plots the intensity values of pixels in a grayscale image.
  - **X-axis**: Represents pixel intensity values (0-255).
  - **Y-axis**: Represents the number of pixels with each intensity value.
- **Usage**: Useful for brightness and contrast analysis, image thresholding, equalization, matching, and object detection.

### 2.2 Color Histogram
- **Definition**: Created separately for each of the three color channels (BGR).
- **Usage**: Used for image classification, color enhancement, segmentation, dominant color extraction, and object recognition.

## 3. Grayscale Histogram Implementation

### 3.1 Load an Image in Grayscale Mode
```python
import cv2
import numpy as np

# Load the image in grayscale mode
img = cv2.imread('image.jpg', 0)
```
- `cv2.imread('image.jpg', 0)`: Loads the image in grayscale mode.

### 3.2 Calculate the Histogram
```python
# Calculate the histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
```
- **Function**: `cv2.calcHist()` calculates the histogram of an image.
  - **Parameters**:
    - `[img]`: The input image (passed as a list).
    - `[0]`: Index of the channel (0 for grayscale).
    - `None`: No mask, the entire image is considered.
    - `[256]`: Number of bins (for intensity values from 0 to 255).
    - `[0, 256]`: Range of pixel values to consider.

### 3.3 Plot the Histogram
```python
import matplotlib.pyplot as plt

# Plot the grayscale histogram
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
```
- **Function**: `plt.plot(hist)` plots the computed histogram, showing the distribution of pixel intensity values in the image.

## 4. Color Histogram Implementation

### 4.1 Load an Image in Color Mode
```python
import cv2
import numpy as np

# Load the image in color mode
img = cv2.imread('image.jpg')
```

### 4.2 Calculate and Plot the Color Histogram
```python
# Initialize colors for BGR channels
colors = ('b', 'g', 'r')

# Loop through each color channel (Blue, Green, Red)
for i, col in enumerate(colors):
    # Calculate the histogram for each channel
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    
    # Plot the histogram for the current channel
    plt.plot(hist, color=col)

plt.title('Color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
```
- **Function**: `cv2.calcHist()` computes the histogram for each color channel (Blue, Green, Red).
  - **Parameters**:
    - `[i]`: Index of the color channel (0 for Blue, 1 for Green, 2 for Red).
    - `plt.plot(hist, color=col)`: Plots the histogram for each channel in its respective color.

## 5. Summary

### 5.1 Grayscale Histogram
- Only one channel, representing the intensity of light from 0 (black) to 255 (white).
- Used to understand image brightness, contrast, and for basic operations like thresholding.

### 5.2 Color Histogram
- Three separate histograms for each color channel (Blue, Green, Red).
- Helps analyze the color distribution in an image, used for tasks like object recognition, color enhancement, and image classification.

## 6. Additional Information and Insights

### 6.1 Grayscale Histogram: Interpretation and Applications

- **Interpretation**:
  - If the histogram is skewed toward the left (lower pixel values), the image is darker.  
  - If the histogram is skewed toward the right (higher pixel values), the image is brighter.

- **Applications**:
  - **Thresholding**: Helps determine suitable threshold values for segmentation.
  - **Contrast Adjustment**: Histogram equalization enhances contrast by spreading pixel values more evenly.

- **Example – Histogram Equalization**:
  - Using OpenCV to improve contrast:
    ```python
    equalized_img = cv2.equalizeHist(img)
    plt.hist(equalized_img.ravel(), 256, [0, 256])
    plt.title('Equalized Histogram')
    plt.show()
    ```
  - This process redistributes pixel intensities, enhancing details in low-contrast images.

### 6.2 Color Histogram: Practical Use Cases

- **Color Distribution**:
  - Analyzing the histogram of each channel can help identify the dominant color in an image. For example:
    - If the Red channel peaks higher than others, the image is more red-dominant.
  
- **Example – Masking Specific Colors**:
  - You can isolate a specific color region using histograms:
    ```python
    lower_blue = np.array([100, 0, 0])
    upper_blue = np.array([255, 50, 50])
    mask = cv2.inRange(img, lower_blue, upper_blue)
    result = cv2.bitwise_and(img, img, mask=mask)
    ```
---

### 6.3 Advanced Histogram Techniques

- **Multi-channel Histogram**:
  - In certain cases, you might want to analyze the relationship between two or more channels. A **2D histogram** shows the joint distribution of two channels:
    ```python
    hist_2d = cv2.calcHist([img], [0, 1], None, [32, 32], [0, 256, 0, 256])
    plt.imshow(hist_2d, interpolation='nearest')
    plt.title('2D Histogram - Blue vs Green')
    plt.show()
    ```
- **Normalized Histogram**:
  - Normalizing histograms ensures the sum of all pixel values equals 1, making it easier to compare histograms of different images:
    ```python
    hist_norm = hist / hist.sum()
    plt.plot(hist_norm)
    plt.title('Normalized Histogram')
    plt.show()
    ```

### 6.4 Histogram Comparison

- **Comparison Metrics**:
  - In some applications (e.g., image retrieval or object detection), you need to compare two histograms using similarity metrics like:
    - **Correlation**
    - **Chi-Square**
    - **Intersection**

- **Example – Histogram Comparison**:
  ```python
  hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
  hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
  similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
  print(f'Similarity Score: {similarity}')
  ```
