# Week 3 OpenCV Lab 3: Basics of Images

### Code Files
- [lab3 sample code.py](lab3_sample_code.py)
- [lab3_practice_code.py](lab3_practice_code.py)

## 1. Basic Image Operations

### 1.1 Resizing Images
- Use `cv2.resize(image, dsize, fx, fy, interpolation)` to resize an image.
  - **Parameters**:
    - `image`: Input image array (single-channel, 8-bit, or floating-point).
    - `dsize`: Desired size of the output image. If not specified, scaling factors `fx` and `fy` are used.
    - `fx`, `fy`: Scale factors along the x (horizontal) and y (vertical) axes.
    - `interpolation`: Interpolation method to use (e.g., `cv2.INTER_LINEAR`, `cv2.INTER_CUBIC`).

```python
import cv2

# Load an image
img = cv2.imread('seal.jpg')

# Resize the image to half its size
resized_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
```

### 1.2 Cropping Images
- To crop an image, use array slicing, which is similar to slicing a NumPy array.
  - **Syntax**: `cropped_img = img[y:y+h, x:x+w]`
    - `y`, `y+h`: Defines the start and end of the height (rows).
    - `x`, `x+w`: Defines the start and end of the width (columns).

```python
# Crop a region from the image
cropped_img = img[50:200, 100:300]
```

### 1.3 Rotating Images
- Use `cv2.rotate(src, rotateCode)` to rotate an image by predefined angles.
  - **Rotate codes**:
    - `cv2.ROTATE_90_CLOCKWISE`
    - `cv2.ROTATE_90_COUNTERCLOCKWISE`
    - `cv2.ROTATE_180`

- To rotate by an arbitrary angle, use `cv2.getRotationMatrix2D(center, angle, scale)` and `cv2.warpAffine()`.

```python
# Rotate image by 90 degrees clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Rotate image by 45 degrees
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img_arbitrary = cv2.warpAffine(img, rotation_matrix, (w, h))
```

## 2. Image Color Spaces and Conversions
- OpenCV loads images in BGR format by default. You can convert images to different color spaces using `cv2.cvtColor()`.

### Common Conversions
- **Convert to Grayscale**: `gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`
- **Convert to HSV**: `hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)`

- **Grayscale** is useful for edge detection, thresholding, and other processing tasks.
- **HSV** (Hue, Saturation, Value) is commonly used for color filtering and segmentation.

```python
# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

## 3. Drawing Shapes and Text
### 3.1 Drawing a Line
- **Syntax**: `cv2.line(image, (x1, y1), (x2, y2), color, thickness)`
  - `(x1, y1)`: Starting point.
  - `(x2, y2)`: Ending point.
  - `color`: Line color in BGR.
  - `thickness`: Thickness in pixels.

### 3.2 Drawing a Rectangle
- **Syntax**: `cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)`

### 3.3 Drawing a Circle
- **Syntax**: `cv2.circle(image, (center_x, center_y), radius, color, thickness)`

### 3.4 Adding Text
- **Syntax**: `cv2.putText(image, text, (x, y), font, fontScale, color, thickness)`
  - `(x, y)`: Bottom-left corner of the text string in the image.
  - `font`: Font type (e.g., `cv2.FONT_HERSHEY_SIMPLEX`).
  - `fontScale`: Scale factor that multiplies the base size of the font.
  - `color`: Text color in BGR.
  - `thickness`: Thickness of the text.

```python
# Draw a rectangle
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)

# Draw a circle
cv2.circle(img, (150, 150), 50, (255, 0, 0), -1)

# Add text to the image
cv2.putText(img, 'OpenCV Lab', (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
```

## 4. Additional Information and Insights

### 4.1 Resizing Images: Insights on Interpolation Methods
- **Choosing the Right Interpolation**:
  - **`cv2.INTER_NEAREST`**: Fastest but can result in pixelation. Useful for simple image scaling, like binary images.
  - **`cv2.INTER_LINEAR`**: Good balance between speed and quality, often the default choice.
  - **`cv2.INTER_CUBIC`**: Higher quality for enlarging images but computationally expensive.
  - **`cv2.INTER_AREA`**: Best suited for downsampling images to retain more detail.

### 4.2 Cropping Images: Managing Image Bounds
- **Slicing Constraints**: 
  - If the crop region goes out of bounds (e.g., trying to slice beyond the image's height or width), OpenCV will raise an **index error**. Always validate the dimensions before cropping.

### 4.3 Rotating Images: Managing Rotation Artifacts
- **Aspect Ratio Changes**: 
  - When rotating by arbitrary angles, parts of the image might go beyond the original frame. To avoid cropping, compute a new bounding box that fits the rotated image:
    ```python
    from math import sin, cos, radians
    angle = 45
    new_w = int(h * abs(sin(radians(angle))) + w * abs(cos(radians(angle))))
    new_h = int(h * abs(cos(radians(angle))) + w * abs(sin(radians(angle))))
    rotated_img_arbitrary = cv2.warpAffine(img, rotation_matrix, (new_w, new_h))
    ```


### 4.4 Image Color Spaces: BGR vs. RGB Confusion
- **BGR vs. RGB**:
  - OpenCV uses BGR by default, which is different from many image libraries (like `PIL`) that use RGB. This can lead to color misrepresentation. For seamless interoperability, convert BGR to RGB when needed:
    ```python
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ```

- **HSV for Filtering**:
  - HSV is great for filtering colors, e.g., to isolate specific color ranges:
    ```python
    lower_bound = (36, 25, 25)  # Light green range
    upper_bound = (86, 255, 255)
    mask = cv2.inRange(hsv_img, lower_bound, upper_bound)
    result = cv2.bitwise_and(img, img, mask=mask)
    ```

### 4.5 Drawing Shapes and Text: Handling Coordinates and Alignment
- **Coordinate Limits**:
  - Coordinates passed to drawing functions must be within the image boundaries. If they exceed the image’s size, OpenCV will raise an error or ignore the out-of-bounds section.
- **Color Format**:
  - The color in OpenCV is represented in BGR. Be mindful of the order when setting colors (e.g., `(255, 0, 0)` is blue, not red).

### 4.6 Saving and Displaying Images
- **Displaying Images**:
  - Use `cv2.imshow()` to display images, but remember to call `cv2.waitKey(0)` to ensure the window doesn’t close immediately:
    ```python
    cv2.imshow('Resized Image', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```
