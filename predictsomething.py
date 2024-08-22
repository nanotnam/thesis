import os
from PIL import Image
import numpy as np

# Define the path to the folder containing the images
folder_path = 'data/masked_UNet'

# Define the path to the folder where processed images will be saved
output_folder_path = 'data/masked_UNet3'

# Create the output folder if it does not exist
os.makedirs(output_folder_path, exist_ok=True)

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
i = 0

# Define the color mapping
color_mapping = {
    0: [255, 255, 255],  # white
    1: [0, 255, 0],      # green
    2: [255, 0, 0]       # red
}

# Loop through each image file
for image_file in image_files:
    # Load the image
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)
    
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Create an empty array with the same shape but with an additional dimension for RGB
    processed_image_array = np.zeros((*image_array.shape, 3), dtype=np.uint8)
    
    # Map the values to the new colors
    for value, color in color_mapping.items():
        processed_image_array[image_array == value] = color
    
    # Convert the numpy array back to an image
    processed_image = Image.fromarray(processed_image_array)
    
    # Save the processed image
    processed_image_path = os.path.join(output_folder_path, image_file)
    processed_image.save(processed_image_path)
    i += 1
    if i % 100 == 0:
        print(f'Processed {i} images')

print(f'\nAll images have been processed and saved to {output_folder_path}.')
