import os
from PIL import Image
import numpy as np

# Directories
gt_dir = 'data/gt3'
processed_dir = 'data/gt4'

if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

# Define the RGB colors for each class
non_building_color = (255, 255, 255)
destroyed_building_color = (255, 0, 0)
not_destroyed_building_color = (0, 255, 0)

color_to_label = {
    non_building_color: 0,
    destroyed_building_color: 2,
    not_destroyed_building_color: 1
}

for file in os.listdir(gt_dir):
    if file.endswith('.png'):
        gt_image = Image.open(os.path.join(gt_dir, file)).convert('RGB')
        gt_array = np.array(gt_image)
        label_map = np.zeros((gt_array.shape[0], gt_array.shape[1]), dtype=np.uint8)

        for color, label in color_to_label.items():
            mask = np.all(gt_array == color, axis=-1)
            label_map[mask] = label

        # Save the label map
        processed_image = Image.fromarray(label_map)
        processed_image.save(os.path.join(processed_dir, file))
