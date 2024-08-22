from PIL import Image
import os
from PIL import ImageFile

# Increase the safety limit to handle large images
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

def split_images_in_folder(input_folder, output_folder, tile_size):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', ".tif")):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            image_width, image_height = image.size

            base_name, ext = os.path.splitext(filename)
            output_subfolder = os.path.join(output_folder, base_name)
            os.makedirs(output_subfolder, exist_ok=True)

            for i in range(0, image_width, tile_size):
                for j in range(0, image_height, tile_size):
                    box = (i, j, i + tile_size, j + tile_size)
                    tile = image.crop(box)
                    tile.save(os.path.join(output_subfolder, f'tile_{i}_{j}.png'))

input_folder = 'data/pre2'
output_folder = 'data/pre3'
tile_size = 256

split_images_in_folder(input_folder, output_folder, tile_size)
