import os
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
import torch.nn as nn

# Path to your dataset folder
dataset_folder = "/Users/hoangnamvu/Documents/code/thesis/data/train1/damage"

# Initialize class counts
class_counts = [0, 0, 0]
a = 0
# Count the number of pixels for each class
for filename in os.listdir(dataset_folder):
    if filename.endswith('.png'):  # or .jpg, .jpeg, etc.
        image_path = os.path.join(dataset_folder, filename)
        image = Image.open(image_path).convert('L')
        image_np = np.array(image)
        for i in range(3):
            class_counts[i] += np.sum(image_np == i)
        a+=1
        if a %200 == 0:
            print(f'gone through {a} files')

# Only consider classes 1 and 2 for weights
class_counts = class_counts[1:]

# Compute class weights as the inverse of the class frequencies
total_pixels = sum(class_counts)
class_weights = [total_pixels / (count + 1e-5) for count in class_counts]

# Normalize weights
class_weights = np.array(class_weights) / sum(class_weights)

print(class_weights)