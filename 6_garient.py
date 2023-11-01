import numpy as np
from scipy.signal import convolve2d
from skimage import io
import matplotlib.pyplot as plt
from skimage import color

def gradient_magnitude(img):
    # Define Sobel filters
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Compute x and y gradients
    grad_x = convolve2d(img, sobel_x, mode='same')
    grad_y = convolve2d(img, sobel_y, mode='same')

    # Compute gradient magnitude
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)

    return grad_mag

def largest_avg_gradient_block(img):
    # Define block size
    block_size = 32

    # Compute gradient magnitude for each block
    grad_mags = []
    for i in range(0, img.shape[0], block_size):
        for j in range(0, img.shape[1], block_size):
            block = img[i:i+block_size, j:j+block_size]
            grad_mag = gradient_magnitude(block).mean()
            grad_mags.append(grad_mag)

    # Find block with largest average gradient magnitude
    max_idx = np.argmax(grad_mags)
    i = (max_idx // (img.shape[1] // block_size)) * block_size
    j = (max_idx % (img.shape[1] // block_size)) * block_size
    largest_block = img[i:i+block_size, j:j+block_size]

    return largest_block


def main():
    # Read the image
    img = io.imread('images/lenna.jpg')

    # Convert the image to grayscale
    img = color.rgb2gray(img)

    # Compute the largest block with the highest average gradient magnitude
    largest_block = largest_avg_gradient_block(img)

    # Display the largest block
    io.imshow(largest_block)
    plt.show()

main()
