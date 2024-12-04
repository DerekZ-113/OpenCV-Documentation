# Week 11 OpenCV Lab 11: Generative AI

## Code Files
- [lab11_sample_code.py](lab11_sample_code.py)
- [lab11 practice code.py](lab11_practice_code.py)

## 1. Introduction to Generative AI
- **Generative AI**: Techniques and models that create new content, such as images, videos, or text.
- **Applications**:
  - Digital Art: Creative artwork generation.
  - Content Creation: Automated design and animation.
  - Medical Imaging: Synthetic CT or MRI scans.
  - Many other use cases.

## 2. Adversarial Images
- **Definition**: Slightly altered images designed to trick AI models.
- **Example**: Misclassifying a “stop” sign as “yield.”
- **Purpose**:
  - Test model robustness.
  - Improve security against adversarial attacks.
- **Technique**:
  - Add noise using methods like FGSM (Fast Gradient Sign Method).

### FGSM Example
```python
import cv2
import numpy as np

# Load original image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Create noise
noise = np.random.normal(0, 25, image.shape).astype('uint8')

# Add noise to create adversarial image
adversarial_image = cv2.addWeighted(image, 1.0, noise, 0.1, 0)

cv2.imshow('Adversarial Image', adversarial_image)
cv2.waitKey(0)
```
- **Function**: `cv2.addWeighted(src1, alpha, src2, beta, gamma)`
  - Combines two arrays (e.g., image and noise) with specified weights.

## 3. Generative Adversarial Networks (GANs)
- **Components**:
  1. **Generator**: Creates fake images from random noise.
  2. **Discriminator**: Distinguishes between real and fake images.
- **Training Objective**:
  - Generator aims to “fool” the discriminator.
  - Discriminator improves to better detect fake images.
  - Uses adversarial loss for simultaneous improvement.

### 3.1 Generator
```python
generator = nn.Sequential(
    nn.Linear(latent_dim, 128),
    nn.ReLU(),
    nn.Linear(128, 256),
    nn.ReLU(),
    nn.Linear(256, 28 * 28),
    nn.Tanh()
)
```
- Produces fake images from noise.

### 3.2 Discriminator
```python
discriminator = nn.Sequential(
    nn.Linear(28 * 28, 256),
    nn.LeakyReLU(0.2),
    nn.Linear(256, 128),
    nn.LeakyReLU(0.2),
    nn.Linear(128, 1),
    nn.Sigmoid()
)
```
- Classifies images as real (1) or fake (0).

### 3.3 Training Loop

#### Discriminator Training
```python
# Real image loss
real_loss = criterion(discriminator(real_imgs), real_labels)

# Fake image loss
fake_loss = criterion(discriminator(fake_imgs.detach()), fake_labels)

# Total loss
d_loss = real_loss + fake_loss
d_loss.backward()
optimizer_D.step()
```

#### Generator Training
```python
# Generator's loss
fake_preds = discriminator(fake_imgs)
g_loss = criterion(fake_preds, real_labels)
g_loss.backward()
optimizer_G.step()
```

## 4. Diffusion Models
- **Purpose**: Handle complex data distributions better than GANs. Generate highly realistic images.
- **Processes**:
  - **Forward**: Gradually corrupt an image with Gaussian noise.
  - **Reverse**: Learn to predict and remove noise using a neural network.

### 4.1 Adding Noise (Forward)
```python
import cv2
import numpy as np

# Load and normalize image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE) / 255.0

# Add Gaussian noise in steps
for i in range(5):
    noise = np.random.normal(0, 0.1 * (i + 1), image.shape)
    noisy_image = np.clip(image + noise, 0, 1)
    cv2.imshow(f"Step {i+1}", (noisy_image * 255).astype('uint8'))
    cv2.waitKey(0)
```
- **Functions**:
  - `np.random.normal`: Generates Gaussian noise.
  - `np.clip`: Ensures pixel values stay within [0, 1].

### 4.2 Denoising (Reverse)
```python
denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)
cv2.imshow("Denoised Image", (denoised_image * 255).astype('uint8'))
cv2.waitKey(0)
```
- **Function**: `cv2.GaussianBlur(src, ksize, sigmaX)`
  - Smooths images by reducing noise.

## 5. Additional Information and Insights

### 5.1 Adversarial Images
- Highlight model vulnerabilities.
- Improve AI model robustness through testing.

### 5.2 GANs
- Ideal for image synthesis but struggle with mode collapse (generating repetitive patterns).
- **Applications**:
  - Image super-resolution.
  - Style transfer.

### 5.3 Diffusion Models
- Produce detailed and diverse outputs.
- Robust in handling complex distributions compared to GANs.

## 6. Summary

### 6.1 Generative AI Overview
- Enables creation of novel content.
- Wide applications in art, content creation, and medicine.

### 6.2 Methods
- **Adversarial Images**:
  - Used to test robustness and improve security.
- **GANs**:
  - Effective for image synthesis but computationally intensive.
- **Diffusion Models**:
  - Handle complex data distributions and produce realistic images.
