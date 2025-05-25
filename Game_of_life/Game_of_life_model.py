#Game of life code
#Author:- Harin Patoliya, 2023

import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

# Read the image file
image = cv2.imread("finimage.png", cv2.IMREAD_COLOR)

# Convert the image to grayscale using OpenCV's cv2.cvtColor function
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

# Read Image as a numpy array
matrix = np.array(grayscale_image)

# Creat initial state for conway's model from grayscale image
# Threshold value for converting grayscale to binary
threshold_value = np.median(grayscale_image)

# Convert the grayscale image to binary using a threshold
binary_image = (grayscale_image > threshold_value).astype(np.uint8)

# Display the binary image
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image (Living=White, Dead=Black)')
plt.axis('off')
plt.show()

# Set initial_state to be the binary image
initial_state = np.array(binary_image)

# Function to calculate the next generation based on Conway's rules
def next_generation(current_state):
    neighbors_count = sum(np.roll(np.roll(current_state, i, 0), j, 1)
                          for i in (-1, 0, 1) for j in (-1, 0, 1) if (i != 0 or j != 0))
    return (neighbors_count == 3) | (current_state & (neighbors_count == 2))

# Set the initial state
current_state = np.array(binary_image)

# Display generations
generations = 100
for generation in range(generations):
    # Calculate the next generation
    current_state = next_generation(current_state)

    # Display the current generation
    plt.imshow(current_state, cmap='gray')
    plt.title(f'Generation {generation + 1}')
    plt.axis('off')
    plt.show()

    # Pause for a short duration to visualize each generation
    time.sleep(0.5)

    # Clear the output for the next generation
    clear_output(wait=True)

print("Simulation completed.")

