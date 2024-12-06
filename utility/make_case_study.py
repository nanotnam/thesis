from PIL import Image
from PIL import ImageFile

# Increase the safety limit to handle large images
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True
# Load the four images
image1 = Image.open("/Users/hoangnamvu/Documents/code/thesis/data/gt1/ant_mask_3/tile_8704_8704.png")
image2 = Image.open("/Users/hoangnamvu/Documents/code/thesis/data/gt1/ant_mask_4/tile_0_8704.png")
image3 = Image.open("/Users/hoangnamvu/Documents/code/thesis/data/gt1/ant_mask_5/tile_8704_0.png")
image4 = Image.open("/Users/hoangnamvu/Documents/code/thesis/data/gt1/ant_mask_6/tile_0_0.png")

# Check if the images are of size 8704x8704
assert image1.size == (8704, 8704)
assert image2.size == (8704, 8704)
assert image3.size == (8704, 8704)
assert image4.size == (8704, 8704)

# Create a new blank image of size 17408x17408
merged_image = Image.new('RGB', (17408, 17408))

# Paste the images into the correct positions
merged_image.paste(image1, (0, 0))
merged_image.paste(image2, (8704, 0))
merged_image.paste(image3, (0, 8704))
merged_image.paste(image4, (8704, 8704))

# Save the merged image
merged_image.save("merged_image.png")