from PIL import Image
import numpy as np

def transform_images(image1_path, image2_path, output_image_path):
    # Open the images
    image1 = Image.open(image1_path).convert('L')  # Convert to grayscale
    image2 = Image.open(image2_path).convert('L')  # Convert to grayscale

    # Convert images to numpy arrays
    image1_array = np.array(image1)
    image2_array = np.array(image2)

    # Create a mask where image1 has pixel value 0
    mask = (image1_array == 0)

    # Apply the mask to image2_array
    output_array = np.where(mask, 0, image2_array)

    # Convert the output array back to an image
    output_image = Image.fromarray(output_array)

    # Save the output image
    output_image.save(output_image_path)

image1_path = 'data/gt4/img1.png'
image2_path = 'data/damageUNetPPmerged/img1.png'
output_image_path = 'data/masked_UNetPP/img1.png'

transform_images(image1_path, image2_path, output_image_path)
