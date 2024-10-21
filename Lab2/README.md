# Week 2 OpenCV Lab 2: Loading, Displaying, and Saving Images

### Code Files
- [lab2_sample_code.py](lab2_sample_code.py)
- [lab2 practice code.py](lab2_practice_code.py)


## 1. Loading Images with OpenCV
**import** the OpenCV library using:
```python
import cv2
```
- Use `cv2.imread(filename)` to load an image from the specified file.
- If the image cannot be read, an empty matrix is returned.

### Three Useful Image Manipulation Flags
- **Syntax**: `gray_img = cv2.imread("image_name.jpg", cv2.IMREAD_GRAYSCALE)`
- `cv2.IMREAD_COLOR` (or `1`): Loads a color image. Any transparency of the image will be neglected. It is the default flag.
- `cv2.IMREAD_GRAYSCALE` (or `0`): Loads an image in grayscale mode.
- `cv2.IMREAD_UNCHANGED` (or `-1`): Loads an image including the alpha channel.

```python
# Load an image in color and grayscale
img = cv2.imread('seal.jpg')
gray_img = cv2.imread('seal.jpg', cv2.IMREAD_GRAYSCALE)
```

## 2. Displaying Images with OpenCV
- Use `cv2.imshow(window_name, image)` to display an image in a window.
- Use `cv2.waitKey()` to display a window for a given time in milliseconds or indefinitely until a key is pressed.
  - `cv2.waitKey(0)`: Waits indefinitely for a key event.
- Use `cv2.destroyAllWindows()` to close all image windows after exiting the script.

```python
# Display the color and grayscale images
cv2.imshow('Color Image', img)
cv2.imshow('Grayscale Image', gray_img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 3. Saving Images with OpenCV
- Use `cv2.imwrite(filename, image)` to save an image to a file.
- The filename must include the desired format extension, such as `.jpg`, `.png`, etc.

```python
# Save the grayscale image
cv2.imwrite('lab_2_image.jpg', gray_img)
```

## 4. Additional Information
### Loading Images with OpenCV
- OpenCV supports various file formats such as PNG, BMP, and TIFF. The use of different `cv2.IMREAD_*` flags can affect how these formats are processed. 
- For example, PNG supports transparency, which can be loaded using `cv2.IMREAD_UNCHANGED`.

### Displaying Images with OpenCV
- The `cv2.waitKey()` function is essential for handling image display, 
- We will use this to display frames from videos in next week.
- Different key codes can be used to control the flow of the display, we will do a mini project about this.

### Saving Images with OpenCV
- OpenCV supports both lossy (e.g., JPEG) and lossless (e.g., PNG) compression. The choice of format can significantly impact the quality and size of the saved image.