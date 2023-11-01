from PIL import Image
import numpy as np

# Create a PIL image from the numpy array
arr = np.array([[43, 73, 93, 71, 35, 36, 53, 27, 45, 17, 76, 13],
                [80, 75, 13, 88, 69, 37, 75, 50, 26, 91, 54, 50],
                [26, 71, 90, 35, 65, 55, 21, 93, 59, 60, 54, 78],
                [92, 13, 67, 92, 61, 43, 31, 89, 94, 41, 25, 33],
                [95, 77, 26, 11, 61, 61, 69, 25, 40, 64, 30, 70],
                [76, 57, 38, 38, 27, 98, 78, 18, 81, 66, 13, 26],
                [69, 62, 26, 68, 97, 91, 33, 95, 53, 55, 36, 21]])
img = Image.fromarray(np.uint8(np.dstack((arr, arr, arr))))

# Save the image to disk
img.save('test.png')
