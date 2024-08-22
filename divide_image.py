from PIL import Image
import os
from PIL import ImageFile

# Increase the safety limit to handle large images
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

def split_image(image_path, tile_size, output_folder, start_index):
    # Open the image
    img = Image.open(image_path)
    img_width, img_height = img.size
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Calculate the number of tiles in both dimensions
    num_tiles_x = img_width // tile_size
    num_tiles_y = img_height // tile_size
    
    tile_number = start_index
    
    for y in range(num_tiles_y):
        for x in range(num_tiles_x):
            # Calculate the box for the tile
            left = x * tile_size
            top = y * tile_size
            right = left + tile_size
            bottom = top + tile_size
            
            # Crop the tile from the image
            tile = img.crop((left, top, right, bottom))
            
            # Save the tile with a descriptive file name
            tile_name = f'image{tile_number}.png'
            tile.save(os.path.join(output_folder, tile_name))
            tile_number += 1

    return tile_number - start_index

def is_image_file(file_path):
    # List of acceptable image file extensions
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.tif']
    _, ext = os.path.splitext(file_path)
    return ext.lower() in image_extensions

def split_images_in_folder(input_folder, tile_size, output_folder):
    # Get a sorted list of image files in the input folder
    image_files = sorted(f for f in os.listdir(input_folder) if is_image_file(os.path.join(input_folder, f)))
    
    # Initialize the starting index for naming output files
    start_index = 1
    
    # Iterate over the sorted list of files
    for filename in image_files:
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path) and is_image_file(file_path):
            # Perform the split image function on the image file
            num_tiles = split_image(file_path, tile_size, output_folder, start_index)
            start_index += num_tiles

# Parameters
input_folder = '/Users/hoangnamvu/Documents/vrije course/thesis/data/test/mask'  # Folder containing the images
tile_size = 8704
output_folder = 'data/gt1'

# Split all images in the folder
split_images_in_folder(input_folder, tile_size, output_folder)


# split_image("/Users/hoangnamvu/Documents/code/thesis/test/ant_mask_1.png", 256, '/Users/hoangnamvu/Documents/code/thesis/test1', 1)