import cv2
import numpy as np
import matplotlib.pyplot as plt


# # Adversarial Images with FGSM
# # Load an image in grayscale
image = cv2.imread('../images/sample_image.jpg', cv2.IMREAD_GRAYSCALE)

# # Create adversarial noise
# noise = np.random.normal(0, 25, image.shape).astype('uint8')

# # Combine image and noise to create adversarial example
# adversarial_image = cv2.addWeighted(image, 1.0, noise, 0.1, 0)

# # Display the adversarial image
# cv2.imshow("Adversarial Image", adversarial_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Generative Adversarial Networks (GANs)
# # Placeholder for GAN setup
# # Example: A generator network
# generator = "Generator code here, typically involves a neural network for image creation"

# # Example: A discriminator network
# discriminator = "Discriminator code here, typically involves a neural network to classify real/fake images"

# # Training process for GANs
# d_loss = "Loss computation for discriminator"
# g_loss = "Loss computation for generator"

# # Diffusion Models
# # Load and preprocess an image for diffusion
# resized_image = cv2.resize(image, (128, 128)) / 255.0  # Normalize to range [0, 1]

# for i in range(5):  # 5 noise addition steps
#     noise = np.random.normal(0, 0.1 * (i + 1), resized_image.shape)
#     noisy_image = np.clip(resized_image + noise, 0, 1)
#     cv2.imshow(f"Step {i+1}", (noisy_image * 255).astype('uint8'))

# # Apply Gaussian blur for denoising
# denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)
# cv2.imshow("Denoised Image", (denoised_image * 255).astype('uint8'))
# cv2.waitKey(0)
# cv2.destroyAllWindows()