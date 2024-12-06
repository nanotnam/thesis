from PIL import Image
from PIL import ImageFile

# Increase the safety limit to handle large images
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

def check_image_dimensions(file_path, expected_width, expected_height):
    try:
        with Image.open(file_path) as img:
            width, height = img.size
            return width == expected_width and height == expected_height
    except Exception as e:
        print(f"Error opening image {file_path}: {e}")
        return False

# Define the expected dimensions
expected_width = 17408
expected_height = 17408

# Define the file paths

png_file_path = '/Users/hoangnamvu/Desktop/testok.png'



# Check the dimensions of the .png file
png_check = check_image_dimensions(png_file_path, expected_width, expected_height)
print(f"The dimensions of the .png file are {'correct' if png_check else 'incorrect'}.")
