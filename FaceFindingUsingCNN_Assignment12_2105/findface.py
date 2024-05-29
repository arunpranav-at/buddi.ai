import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.signal as sp

# Open the images
bigImageColor = Image.open("groupphoto.jpg")
smallImageColor = Image.open("dhoniphoto.jpg")

# Display the big image
fig1 = plt.figure()
plt.imshow(bigImageColor, cmap='gray')
plt.title("Big Image")
plt.show()

# Display the small image
fig2 = plt.figure()
plt.imshow(smallImageColor, cmap='gray')
plt.title("Small Image")
plt.show()

# Convert to grayscale
bigImage = bigImageColor.convert('L')
smallImage = smallImageColor.convert('L')

# Convert the images to arrays and normalize them
arrayBigImg = np.array(bigImage, dtype=np.float64)
arraySmallImg = np.array(smallImage, dtype=np.float64)

# Normalize the arrays
arrayBigImg = (arrayBigImg - np.mean(arrayBigImg)) / np.std(arrayBigImg)
arraySmallImg = (arraySmallImg - np.mean(arraySmallImg)) / np.std(arraySmallImg)

# Print the shape of the images
print("Big Image shape:", arrayBigImg.shape)
print("Small Image shape:", arraySmallImg.shape)

# Convolve the big image with the small image
result = sp.convolve2d(arrayBigImg, arraySmallImg[::-1, ::-1], mode='same')

# Find the location of the peak in the result
y, x = np.unravel_index(np.argmax(result), result.shape)

# Display the big image with a rectangle showing the location of the small image
fig3 = plt.figure()
plt.imshow(bigImageColor)
plt.title("Detected Location")

# Create a rectangle around the detected area
rect = plt.Rectangle((x - arraySmallImg.shape[1]//2, y - arraySmallImg.shape[0]//2), arraySmallImg.shape[1], arraySmallImg.shape[0], edgecolor='r', facecolor='none', linewidth=10)
plt.gca().add_patch(rect)
# Print the location of the detected area
print("Detected location:", x, y)
plt.show()

fig4 = plt.figure()
plt.imshow(result)
plt.title("Result")
plt.show()