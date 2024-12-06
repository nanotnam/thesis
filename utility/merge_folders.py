from PIL import Image
import os
from PIL import ImageFile

# Increase the safety limit to handle large images
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True
def merge_images_in_folder(input_folder, output_folder, original_size, tile_size):
    os.makedirs(output_folder, exist_ok=True)

    for subfolder in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder)
        if os.path.isdir(subfolder_path):
            merged_image = Image.new('RGB', original_size)

            for i in range(0, original_size[0], tile_size):
                for j in range(0, original_size[1], tile_size):
                    tile_path = os.path.join(subfolder_path, f'tile_{i}_{j}.png')
                    if os.path.exists(tile_path):
                        tile = Image.open(tile_path)
                        merged_image.paste(tile, (i, j))

            merged_image.save(os.path.join(output_folder, f'{subfolder}.png'))

input_folder = '/Users/hoangnamvu/Downloads/ccc/damageUNetPP'
output_folder = 'data/damageUNetPPmerged'
original_size = (8704, 8704)
tile_size = 256

merge_images_in_folder(input_folder, output_folder, original_size, tile_size)

