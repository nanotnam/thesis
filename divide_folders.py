import os
import shutil

# Paths to the original folders
base_folder = '/Users/hoangnamvu/Documents/vrije course/thesis/final_data/train_set'
pre_folder = os.path.join(base_folder, 'pre')
post_folder = os.path.join(base_folder, 'post')
gt_folder = os.path.join(base_folder, 'gt')

# List all files in the folders
pre_files = sorted(os.listdir(pre_folder))
post_files = sorted(os.listdir(post_folder))
gt_files = sorted(os.listdir(gt_folder))

# Count the number of files in each folder
num_pre_files = len(pre_files)
num_post_files = len(post_files)
num_gt_files = len(gt_files)

# Number of parts to divide into
num_parts = 6

# Function to divide files into parts
def divide_files(files, num_parts):
    avg = len(files) / float(num_parts)
    out = []
    last = 0.0

    while last < len(files):
        out.append(files[int(last):int(last + avg)])
        last += avg

    return out

# Divide each folder's files into parts
pre_parts = divide_files(pre_files, num_parts)
post_parts = divide_files(post_files, num_parts)
gt_parts = divide_files(gt_files, num_parts)

# Create new folders and distribute the files
for i in range(num_parts):
    # Create new subfolders for each part
    part_folder = os.path.join(base_folder, f'part{i+1}')
    os.makedirs(part_folder, exist_ok=True)
    os.makedirs(os.path.join(part_folder, 'pre'), exist_ok=True)
    os.makedirs(os.path.join(part_folder, 'post'), exist_ok=True)
    os.makedirs(os.path.join(part_folder, 'gt'), exist_ok=True)

    # Move files to the new subfolders
    for pre_file in pre_parts[i]:
        shutil.move(os.path.join(pre_folder, pre_file), os.path.join(part_folder, 'pre', pre_file))
    for post_file in post_parts[i]:
        shutil.move(os.path.join(post_folder, post_file), os.path.join(part_folder, 'post', post_file))
    for gt_file in gt_parts[i]:
        shutil.move(os.path.join(gt_folder, gt_file), os.path.join(part_folder, 'gt', gt_file))

print("Files have been successfully divided into 6 parts.")
