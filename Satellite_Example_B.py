import numpy as np
# from scipy import misc
import imageio
import matplotlib.pyplot as plt
from skimage import data
import skimage
import random

# read photo
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')

# create multidimentional ndarray operation in single line, showing vertors
total_rows, total_cols, total_layers = photo_data.shape
print(photo_data.shape)
print(total_rows)
print(total_cols)
print(total_layers)
X, Y = np.ogrid[:total_rows, :total_cols]
print("X= ", X.shape, "Y= ", Y.shape)

# creat center of the mask
center_rows, center_cols = total_rows / 2, total_cols / 2
# calculate distance to center
# print(X - center_rows)
# print(Y - center_cols)
dist_from_center = np.sqrt((X - center_rows)**2 + (Y - center_cols)**2)
# print(dist_from_center)

# calculate radius for the mask wanted
radius = (total_rows/2)
# if distance from center > r, then apply mask to have data = 0
circular_mask = (dist_from_center > radius)
print(circular_mask)
photo_data[circular_mask] = 0
plt.figure(figsize = (15,15))
plt.imshow(photo_data)

# further masking, to just get upper half disc.
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
X2, Y2 = np.ogrid[:total_rows, :total_cols]
half_upper = X2 < center_rows
half_upper_mask = np.logical_and(half_upper, circular_mask)
# if its under half_upper_mask then show white
# photo_data[half_upper_mask] = 255
# if its under half_upper_mask then show random from 200-255
photo_data[half_upper_mask] = random.randint(200,255)
plt.figure(figsize = (15,15))
plt.imshow(photo_data)

# Processing of red pixels
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
# (r,g,b) = (0,1,2)
red_mask = photo_data[:, :, 0] <150
photo_data[red_mask] = 0
plt.figure(figsize = (15,15))
plt.imshow(photo_data)

# Composite mask that takes thresholds on all three rgb layers
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
red_mask = photo_data[:, :, 0] <150
green_mask = photo_data[:, :, 1] > 100
blue_mask = photo_data[:, :, 2] < 100
final_mask = np.logical_and(red_mask, green_mask, blue_mask)
photo_data[final_mask] = 0
plt.figure(figsize = (15,15))
plt.imshow(photo_data)

plt.show()