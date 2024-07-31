import cv2
import numpy as np

# Load the image
image = cv2.imread('image1.png')

# Draw a red dot at (x, y)
x, y = 100, 200
cv2.circle(image, (x, y), 50, (0, 0, 255), -1)  # Red dot

# Save the modified image
cv2.imwrite('annotated_image.jpg', image)
