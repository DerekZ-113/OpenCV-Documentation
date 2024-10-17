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