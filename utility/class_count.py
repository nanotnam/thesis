import os
import numpy as np
from PIL import Image


# Path to your dataset folder
dataset_folder = "data/train1/seg_post"

# Initialize class counts
class_counts = [0, 0]
# Count the number of pixels for each class
for filename in os.listdir(dataset_folder):
    if filename.endswith('.png'):  # or .jpg, .jpeg, etc.
        image_path = os.path.join(dataset_folder, filename)
        image = Image.open(image_path).convert('L')
        image_np = np.array(image)
        for i in range(2):
            class_counts[i] += np.sum(image_np == i)

print(class_counts)