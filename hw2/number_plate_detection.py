
import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = '00.jpg'  # Update this path with the actual image path
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur for smoothing
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Detect vertical edges using Sobel operator
sobel_vertical = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
abs_sobel_vertical = cv2.convertScaleAbs(sobel_vertical)

# Apply binary thresholding
_, threshold_image = cv2.threshold(abs_sobel_vertical, 100, 255, cv2.THRESH_BINARY)

# Perform morphological operations (closing and erosion)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 3))
morph_close = cv2.morphologyEx(threshold_image, cv2.MORPH_CLOSE, kernel)
morph_erode = cv2.erode(morph_close, kernel)

# Plot the original and processed images
fig, ax = plt.subplots(1, 4, figsize=(24, 10))
ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
ax[0].set_title('① Original Image')
ax[1].imshow(abs_sobel_vertical, cmap='gray')
ax[1].set_title('② Vertical Edge Detection')
ax[2].imshow(threshold_image, cmap='gray')
ax[2].set_title('③ Thresholding (Binary)')
ax[3].imshow(morph_erode, cmap='gray')
ax[3].set_title('④ Morphological Operations (Closing + Erosion)')

for a in ax:
    a.axis('off')

plt.show()
