import os
from PIL import Image
import numpy as np

# Define the input and output directories
input_dir = 'data/test1/damage'
output_dir = 'data/test1/seg_post'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define the transformation function
# def transform_pixels(image_array):
#     transformed_array = np.copy(image_array)
#     transformed_array[(image_array == 1) | (image_array == 2)] = 1
#     transformed_array[(image_array == 3) | (image_array == 4)] = 0
#     return transformed_array

def transform_pixels(image_array):
    transformed_array = np.copy(image_array)
    transformed_array[(image_array == 2)] = 0
    return transformed_array

# Process each image in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # Load the image
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)
        image_array = np.array(image)

        # Transform the image
        transformed_array = transform_pixels(image_array)

        # Save the transformed image
        transformed_image = Image.fromarray(transformed_array)
        output_path = os.path.join(output_dir, filename)
        transformed_image.save(output_path)

print("Image transformation complete.")

