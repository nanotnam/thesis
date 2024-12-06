from PIL import Image
import numpy as np

# Load the image
image_path = 'data/masked_UNet/img1.png'
image = Image.open(image_path)

# Convert the image to a numpy array
image_array = np.array(image)

# Get the unique values in the array
unique_colors = np.unique(image_array)

# Count the number of unique values
num_unique_colors = len(unique_colors)

print(f'The image has {num_unique_colors} unique colors.')

print(unique_colors)