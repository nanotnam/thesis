import os
from PIL import Image
import numpy as np

# Define the path to the folder containing the images
folder_path = 'data/gt4'

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Set to store unique colors
all_unique_colors = set()
i =0
# Loop through each image file
for image_file in image_files:
    # Load the image
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)
    
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Get the unique values in the array
    unique_colors = np.unique(image_array)
    
    # Add unique colors to the set
    for color in unique_colors:
        all_unique_colors.add(color)
    
    # Count the number of unique values
    num_unique_colors = len(unique_colors)
    i+=1
    if i%100 ==0:
        print(f"checked {i} images")

# Convert the set to a list to print it
all_unique_colors_list = list(all_unique_colors)
num_all_unique_colors = len(all_unique_colors_list)

print(f'\nThe total number of unique colors in all images is {num_all_unique_colors}.')
print(all_unique_colors_list)
