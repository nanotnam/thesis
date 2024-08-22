import os

def rename_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate through each file
    for filename in files:
        # Check if the file ends with '_pre_disaster.png'
        if filename.endswith('_pre_disaster.png'):
            # Construct the new filename by removing '_pre_disaster'
            new_filename = filename.replace('_pre_disaster', '')
            # Full paths to the old and new files
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {old_filepath} to {new_filepath}")

# Example usage
folder_path = '/Users/hoangnamvu/Downloads/training_data/pre'
rename_files(folder_path)
