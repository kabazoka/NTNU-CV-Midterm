import matplotlib.pyplot as plt
import numpy as np
from skimage import io
import math
import random

fig = plt.figure('images/lenna.jpg', figsize=(10,10))
ax = fig.add_subplot(1,1,1)

def rgb_to_gray(rgb_image):
    gray_image = np.max(rgb_image, axis=2)
    return gray_image

def main():
    # Read the image
    # fig = plt.figure('images/lenna.jpg', figsize=(10,10))

    # Convert the image to grayscale
    gray_image = rgb_to_gray(fig)
    
    # Display the grayscale image
    ax.imshow(gray_image, cmap='gray')
    plt.show()

main()