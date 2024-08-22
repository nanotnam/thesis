import os
import shutil

def move_images_by_suffix(source_folder, pre_disaster_folder, post_disaster_folder):
    # Ensure destination folders exist
    if not os.path.exists(pre_disaster_folder):
        os.makedirs(pre_disaster_folder)
    if not os.path.exists(post_disaster_folder):
        os.makedirs(post_disaster_folder)

    # Get all files in the source folder
    files = os.listdir(source_folder)

    # Process each file
    for file_name in files:
        if file_name.endswith('pre_disaster_target.png'):
            # Move pre-disaster image to pre_disaster_folder
            shutil.move(os.path.join(source_folder, file_name), os.path.join(pre_disaster_folder, file_name))
            print(f"Moved {file_name} to {pre_disaster_folder}")
        elif file_name.endswith('post_disaster_target.png'):
            # Move post-disaster image to post_disaster_folder
            shutil.move(os.path.join(source_folder, file_name), os.path.join(post_disaster_folder, file_name))
            print(f"Moved {file_name} to {post_disaster_folder}")

# Example usage
source_folder = 'data/train1/targets'
pre_disaster_folder = 'data/train1/gt_pre'
post_disaster_folder = 'data/train1/gt_post'

move_images_by_suffix(source_folder, pre_disaster_folder, post_disaster_folder)
