from PIL import Image
import torchvision.transforms as transforms
import torch

def image_to_tensor(image_path):
    # Open the image using PIL
    img = Image.open(image_path).convert('RGB')
    
    # Define a transform to convert the image to a PyTorch tensor
    transform = transforms.ToTensor()
    
    # Apply the transform to the image
    img_tensor = transform(img)
    
    return img_tensor

# Example usage
image_path = '/Users/hoangnamvu/Documents/code/thesis/pre/ant_pre_1_0.png'
img_tensor = image_to_tensor(image_path)

# Print the tensor and its shape
print(img_tensor)
print(img_tensor.shape)
