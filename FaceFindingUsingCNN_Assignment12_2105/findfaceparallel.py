import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.signal as sp
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to compute cross-correlation for a given range of rows
def cross_correlate_chunk(start_row, end_row, arrayBigImg, arraySmallImg):
    return sp.convolve2d(arrayBigImg[start_row:end_row, :], arraySmallImg[::-1, ::-1], mode='same')

# Open the images
bigImageColor = Image.open("groupphoto.jpg")
smallImageColor = Image.open("dhoniphoto.jpg")

# Display the big image
plt.imshow(bigImageColor, cmap='gray')
plt.title("Big Image")
plt.show()

# Display the small image
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

# Number of chunks for parallel processing
num_chunks = 8
chunk_size = arrayBigImg.shape[0] // num_chunks
chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_chunks)]
if arrayBigImg.shape[0] % num_chunks != 0:
    chunks[-1] = (chunks[-1][0], arrayBigImg.shape[0])

# Perform cross-correlation in parallel
results = []
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(cross_correlate_chunk, start, end, arrayBigImg, arraySmallImg) for start, end in chunks]
    for future in as_completed(futures):
        results.append(future.result())

# Combine the results from each chunk
result = np.vstack(results)

# Find the location of the peak in the result
y, x = np.unravel_index(np.argmax(result), result.shape)

# Display the big image with a rectangle showing the location of the small image
plt.imshow(bigImageColor)
plt.title("Detected Location")

# Create a rectangle around the detected area
rect = plt.Rectangle((x - arraySmallImg.shape[1]//2, y - arraySmallImg.shape[0]//2), arraySmallImg.shape[1], arraySmallImg.shape[0], edgecolor='r', facecolor='none', linewidth=10)
plt.gca().add_patch(rect)
plt.show()