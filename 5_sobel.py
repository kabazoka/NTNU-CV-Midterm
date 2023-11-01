import matplotlib.pyplot as plt
import numpy as np
from skimage import io
import math
import random

def convolve(image, kernel):
    # Get the dimensions of the image and kernel
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate the padding needed for the convolution
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Create a padded image with zeros
    padded_image = np.zeros((image_height + pad_height * 2, image_width + pad_width * 2))
    padded_image[pad_height:-pad_height, pad_width:-pad_width] = image

    # Create an output image with zeros
    output_image = np.zeros((image_height, image_width))

    # Convolve the image with the kernel
    for i in range(pad_height, image_height + pad_height):
        for j in range(pad_width, image_width + pad_width):
            output_image[i - pad_height, j - pad_width] = np.sum(kernel * padded_image[i - pad_height:i + pad_height + 1, j - pad_width:j + pad_width + 1])

    return output_image

# Load the image
image = io.imread('images/lenna.jpg', as_gray=True)

# Define the Sobel edge detectors
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Convolve the image with the Sobel edge detectors
sobel_x_image = convolve(image, sobel_x)
sobel_y_image = convolve(image, sobel_y)

# Display the results
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(1, 3, 1)
ax1.imshow(image, cmap='gray')
ax1.set_title('Original Image')
ax2 = fig.add_subplot(1, 3, 2)
ax2.imshow(sobel_x_image, cmap='gray')
ax2.set_title('Sobel X')
ax3 = fig.add_subplot(1, 3, 3)
ax3.imshow(sobel_y_image, cmap='gray')
ax3.set_title('Sobel Y')
plt.show()

