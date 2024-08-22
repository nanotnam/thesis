from PIL import Image
import numpy as np
from PIL import ImageFile

# Increase the safety limit to handle large images
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Function to print RGB values of an image
def print_rgb_values(image_path):
    # Load image
    image = Image.open(image_path).convert('L')
    image_np = np.array(image)

    # Print RGB values
    print("RGB values of the image:")
    print(image_np)

# Example usage
image_path = "/Users/hoangnamvu/Documents/vrije course/thesis/final_data/train_set/gt1/image1.png"  # Replace with your image path
print_rgb_values(image_path)