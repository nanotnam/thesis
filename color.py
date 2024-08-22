import os
from PIL import Image
import numpy as np
from PIL import ImageFile

# Increase the safety limit to handle large images
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True


# RGB values for white, green, and red in 0-255 range
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

# Function to replace each pixel with the closest color among white, green, and red
def replace_with_closest_color(image_path):
    # Load image
    image = Image.open(image_path).convert('RGB')
    image_np = np.array(image)

    # Define the three colors
    colors = np.array([WHITE, GREEN, RED])

    # Reshape the image array to a 2D array of pixels
    pixels = image_np.reshape(-1, 3)

    # Calculate the Euclidean distance to each color
    distances = np.linalg.norm(pixels[:, None] - colors, axis=2)

    # Find the index of the closest color for each pixel
    closest_color_indices = np.argmin(distances, axis=1)

    # Replace each pixel with the closest color
    new_pixels = colors[closest_color_indices].reshape(image_np.shape)

    # Convert back to image
    new_image = Image.fromarray(new_pixels.astype('uint8'))

    return new_image

# Input and output directories
input_dir = "data/gt2"
output_dir = "data/gt3"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each image
for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        # Process each image
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Replace each pixel with the closest color
        new_image = replace_with_closest_color(input_path)

        # Save the new image
        new_image.save(output_path)

        print(f"Processed: {filename}")

print("All images processed.")
