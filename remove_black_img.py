from PIL import Image
import os

def is_all_black(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')  # Ensure the image is RGB (in case it's grayscale)
        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                if r != 0 or g != 0 or b != 0:
                    return False
        return True
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False
    

def remove_images_if_all_black(folder1, folder2, folder3):
    for filename in os.listdir(folder1):
        if filename.endswith('.png'):  # Adjust file extension as needed
            image_path1 = os.path.join(folder1, filename)
            image_path2 = os.path.join(folder2, filename)
            image_path3 = os.path.join(folder3, filename)

            if is_all_black(image_path1):
                print(f"Removing {filename}...")
                os.remove(image_path1)
                os.remove(image_path2)
                os.remove(image_path3)


if __name__ == "__main__":
    folder1 = "data/test1/pre"
    folder2 = "data/test1/post"
    folder3 = "data/test1/gt2"

    remove_images_if_all_black(folder1, folder2, folder3)
