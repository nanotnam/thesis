import os
from PIL import Image
import numpy as np
from sklearn.metrics import f1_score

def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".png"):  # Assuming the images are in PNG format
            img = Image.open(os.path.join(folder, filename))
            if img is not None:
                images.append(np.array(img))
    return images

def calculate_f1_score(folder1, folder2):
    images1 = load_images_from_folder(folder1)
    images2 = load_images_from_folder(folder2)
    
    assert len(images1) == len(images2), "Folders must contain the same number of images."
    
    all_pixels1 = np.concatenate([img.flatten() for img in images1])
    all_pixels2 = np.concatenate([img.flatten() for img in images2])
    
    f1_score_1 = f1_score(all_pixels1, all_pixels2, labels=[1], average='macro')
    f1_score_2 = f1_score(all_pixels1, all_pixels2, labels=[2], average='macro')
    
    return f1_score_1, f1_score_2

folder1 = 'data/gt4'
folder2 = 'data/masked_UNetPP'

f1_score_1, f1_score_2 = calculate_f1_score(folder1, folder2)

print(f"F1 Score for pixel value 1: {f1_score_1}")
print(f"F1 Score for pixel value 2: {f1_score_2}")