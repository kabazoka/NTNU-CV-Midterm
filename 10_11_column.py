import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
from PIL import Image
import requests

link = "https://i.postimg.cc/3RN2T4SB/east-coast-taiwan-header.jpg"
dImageSlice = 10

origImage = Image.open( requests.get(link, stream=True).raw )
oimg = np.array( origImage )

# Calculate the column histogram for the input image
# First, break the image into 10 slices that run from top to bottom
height, width, channels = oimg.shape
slice_height = height // dImageSlice
slices = [oimg[i*slice_height:(i+1)*slice_height,:,:] for i in range(dImageSlice)]

# Then, sum up all pixel values in the green channel for each slice and store it in a 10 sized vector
green_channel = slices[0][:,:,1]
column_hist = np.zeros(dImageSlice)
for i in range(dImageSlice):
    green_channel = slices[i][:,:,1]
    column_hist[i] = np.sum(green_channel)

# Normalize the column histogram vector using L2-norm
column_hist_norm = column_hist / np.linalg.norm(column_hist)

print(column_hist_norm)



