import os
from PIL import Image
import numpy as np

# Define the path to the folder containing the images
folder_path = '/Users/hoangnamvu/Downloads/train/targets/'

# Define the paths to the folders where processed images will be saved
pre_disaster_folder = '/Users/hoangnamvu/Documents/code/thesis/xbd_target_pre'
post_disaster_folder = '/Users/hoangnamvu/Documents/code/thesis/xbd_target_post'

# Create the output folders if they do not exist
os.makedirs(pre_disaster_folder, exist_ok=True)
os.makedirs(post_disaster_folder, exist_ok=True)

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
    
    # Update pixel values: 1 and 2 become 1, and 3 and 4 become 2
    image_array[np.isin(image_array, [1, 2])] = 1
    image_array[np.isin(image_array, [3, 4])] = 2
    
    # Convert the numpy array back to an image
    processed_image = Image.fromarray(image_array)
    
    # Determine the output folder based on the filename
    if image_file.endswith('pre_disaster_target.png'):
        processed_image_path = os.path.join(pre_disaster_folder, image_file)
    elif image_file.endswith('post_disaster_target.png'):
        processed_image_path = os.path.join(post_disaster_folder, image_file)
    else:
        continue  # Skip files that do not match the expected patterns
    
    # Save the processed image
    processed_image.save(processed_image_path)
    i+=1
    if i%100 == 0:
        print(f'Processed {i} images')

print(f'\nAll images have been processed and saved to the respective folders.')
