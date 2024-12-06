import os
import json
from PIL import Image, ImageDraw
from shapely import wkt
import glob

def process_json_file(json_path, output_folder, damage_mapping):
    # Load the JSON data
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Extract metadata and features
    metadata = data['metadata']
    features = data['features']['xy']

    # Create a blank image with the specified dimensions
    width, height = metadata['width'], metadata['height']
    image = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(image)

    # Draw each polygon with the appropriate damage value
    for feature in features:
        subtype = feature['properties']['subtype']
        value = damage_mapping.get(subtype, 0)
        polygon = wkt.loads(feature['wkt'])
        polygon_coords = [(x, y) for x, y in polygon.exterior.coords]
        draw.polygon(polygon_coords, fill=value)

    # Save the image as a greyscale PNG with a name corresponding to the original JSON file
    base_filename = os.path.splitext(os.path.basename(json_path))[0]
    output_path = os.path.join(output_folder, f"{base_filename}.png")
    image.save(output_path)
    print(f"Saved image: {output_path}")

def process_json_folder(input_folder, output_folder):
    # Define a mapping for damage subtypes
    damage_mapping = {
        'no-damage': 1,
        'minor-damage': 1,
        'major-damage': 2,
        'destroyed': 2
    }

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all JSON files in the input folder
    json_files = glob.glob(os.path.join(input_folder, '*.json'))

    # Process each JSON file
    for json_file in json_files:
        process_json_file(json_file, output_folder, damage_mapping)

# Example usage
input_folder = '/Users/hoangnamvu/Downloads/tier3/labels'
output_folder = '/Users/hoangnamvu/Downloads/tier3/targets'
process_json_folder(input_folder, output_folder)

