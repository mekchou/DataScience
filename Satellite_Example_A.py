# %matplotlib inline
import numpy as np
# from scipy import misc
import imageio
import matplotlib.pyplot as plt
from skimage import data
import skimage

# read photo
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
# check photo type
print(type(photo_data))
# set photo size
plt.figure(figsize=(15,15))
# to show graph. must plt.show in python, different than jupiter
# plt.imshow(photo_data)
# plt.show()
# print photo shape, (length,width,3 layers of color(RGB))
# in this photo, red = altitude, blue = aspect, green = slope
print(photo_data.shape)

# show array 
# print(photo_data)

print(photo_data.size)
print(photo_data.min(),photo_data.max())
print(photo_data.mean())
# show [r,g,b] for specific pixel
print(photo_data[150,250])
# show value for green on specific pixel (0,1,2) = (r,g,b)
print(photo_data[150,250,1])

# change value of a pixel
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
photo_data[150,250] = 0
plt.figure(figsize=(15,15))
# plt.imshow(photo_data)
# plt.show()

# change a range of pixel's green
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
photo_data[150:200, 150:550, 1] = 255
plt.figure(figsize=(10,10))
# plt.imshow(photo_data)

# change a range of pixel
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
photo_data[150:200, :] = 255
plt.figure(figsize=(10,10))
# plt.imshow(photo_data)

# pick all pixels with low values
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
print("Shape of photo data:", photo_data.shape)
low_value_filter = photo_data < 150
print("Shape of photo data:", low_value_filter.shape)
plt.figure(figsize=(10,10))
# plt.imshow(photo_data)
photo_data[low_value_filter] = 150
plt.figure(figsize=(10,10))
# plt.imshow(photo_data)

#  more columns and rows operaion
photo_data = imageio.imread('./numpy_satellite/wifire/sd-3layers.jpg')
rows_range = np.arange(len(photo_data))
cols_range = rows_range
print(type(rows_range))
print(rows_range,cols_range)
photo_data[rows_range, cols_range] = 255
plt.figure(figsize=(15,15))
plt.imshow(photo_data)

plt.show()