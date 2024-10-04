## Week 2 OpenCV Lab 2

# Loading, displaying, and saving images  

## 1. Loading images with OpenCV
**Import** OpenCV libaray first using `import cv2`  
Load an image from a file use function in cv2 library as following `img = cv2.imread("image_name.jpg")  
If the image cannot be read, empty matrix will be returned  
  
### Three useful image manipulation functions
- Syntax: `gray_img = cv2.imread("image_name.jpg", cv2.IMREAD_GRAYSCALE)`  
- `cv2.IMREAD_COLOR` specify to load a color image. Any transparency of the image will be neglected. It is the default flag. Alternatively, pass integer value 1 for this flag.  
- `cv2.IMREAD_GRAYSCALE` specify to load an image in grayscale mode. Or pass integer value 0 for this flag.  
- `cv2.IMREAD_UNCHANGED` specify to load an image including alpha channel. Or pass integer value 1 for this flag.  
  
## 2. Displaying images with OpenCV  
- `cv2.imshow(window_name, image)` 
    - method to display an image in a window  
- `cv2.waitKey()`  
    - Allows to display a window for given milliseconds or until any key is pressed.  
    - Takes time in milliseconds as a parameter, and wait for the given time to destroy the window. 0 as argument will wait until any key is pressed.  
- `cv2.destroyAllWindows()`  
    - destroy all windows at any time after exiting the script.  
  
## Saving images with OpenCV
- `cv2.imwrite(filename, image)`
    - file name must include image format.