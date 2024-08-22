import os
from PIL import Image
import numpy as np

# Define the path to the folder containing the images
folder_path = 'data/masked_UNetPP'

# Define the path to the folder where processed images will be saved
output_folder_path = 'data/masked_UNetPP2'

# Create the output folder if it does not exist
os.makedirs(output_folder_path, exist_ok=True)

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
i = 0
# Loop through each image file
for image_file in image_files:
    # Load the image
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)
    
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Change all pixels with a value of 0 to 255
    image_array[image_array == 0] = 255
    image_array[image_array == 1] = 200
    image_array[image_array == 2] = 0
    
    # Convert the numpy array back to an image
    processed_image = Image.fromarray(image_array)
    
    # Save the processed image
    processed_image_path = os.path.join(output_folder_path, image_file)
    processed_image.save(processed_image_path)
    i+=1
    if i % 100 == 0:
        print(f'Processed {i} images')

print(f'\nAll images have been processed and saved to {output_folder_path}.')
