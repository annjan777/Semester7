# Import necessary libraries
import cv2
import matplotlib.pyplot as plt
# Function to display images using Matplotlib
def display_image(title, image, cmap=None):
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis('off')
    plt.show()
# Path to the input image
image_path = '/Users/annjan/Desktop/Semester7/Computer Vision/Experiment1/culogo.png'
# Reading the image file
image = cv2.imread(image_path)
# Converting the image to different color models
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
# Display each converted image using Matplotlib
display_image('RGB Image', image_rgb)
display_image('Grayscale Image', image_gray, cmap='gray')
display_image('HSV Image', image_hsv)
display_image('Lab Image', image_lab)
# Saving the processed images
cv2.imwrite('image_gray.jpg', image_gray)
cv2.imwrite('image_hsv.png', image_hsv)
cv2.imwrite('image_lab.bmp', image_lab)
